"""Archive the two user-owned skill roots without system/plugin caches or runtime state."""
import hashlib
import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROOTS = {"agents": Path.home()/'.agents/skills', "codex": Path.home()/'.codex/skills'}
SKIP_DIRS = {'.git', '.system', '__pycache__', 'node_modules', '.venv', 'venv', '.pytest_cache', '.ruff_cache', '.mypy_cache', '.cache'}
SKIP_SUFFIX = {'.pyc', '.pyo', '.log', '.sqlite', '.sqlite3', '.db', '.pem', '.key', '.pfx', '.p12'}
SECRET = re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-proj-[A-Za-z0-9_-]{35,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')

def digest_file(path):
    data=path.read_bytes()
    try:
        data.decode('utf-8')
        if b'\0' not in data:
            data=data.replace(b'\r\n',b'\n')
    except UnicodeDecodeError:
        pass
    return hashlib.sha256(data).hexdigest()

def files(root):
    for current, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not (Path(current)/d).is_symlink())
        for name in sorted(names):
            p=Path(current)/name
            if p.is_symlink() or p.suffix.lower() in SKIP_SUFFIX or name in {'Thumbs.db','.DS_Store','.env','.env.local','.env.production','credentials.json','auth.json'}:
                continue
            yield p

def inventory(root):
    return {p.relative_to(root).as_posix():digest_file(p) for p in files(root)}

def copy_snapshot(source, dest, inv):
    for rel, digest in inv.items():
        p=dest/rel
        if not p.exists() or digest_file(p)!=digest:
            p.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(source/rel,p)

def main():
    manifest=json.loads((REPO/'skills-manifest.json').read_text(encoding='utf-8-sig'))
    old={(x['target'],x['name']):x for x in manifest['skills']}
    categories=manifest['categories']
    categories['career-job-search']='Resume preparation, career evidence, interviews, and job application workflows.'
    individual=[]; packages=[]; rows=[]; duplicates=defaultdict(list); issues=[]
    for target,root in ROOTS.items():
        for source in sorted(root.iterdir()):
            if not source.is_dir() or source.name in SKIP_DIRS:
                continue
            inv=inventory(source)
            skillpaths=sorted(p for p in inv if p=='SKILL.md' or p.endswith('/SKILL.md'))
            if not skillpaths:
                continue
            for rel in inv:
                p=source/rel
                if p.stat().st_size<3_000_000 and p.suffix.lower() in {'.md','.json','.py','.sh','.ps1','.js','.mjs','.cjs','.toml','.yml','.yaml','.txt'}:
                    if SECRET.search(p.read_text(encoding='utf-8',errors='replace')):
                        issues.append(f'{target}/{source.name}/{rel}')
            if skillpaths==['SKILL.md']:
                previous=old.get((target,source.name))
                category=previous['category'] if previous else ('writing-language' if source.name=='humanizer' else 'frontend-ui-design' if source.name=='fresh-cartoon-frontend' else 'tools-productivity')
                path=previous['path'] if previous else f'skills/{category}/{source.name}'
                record={'name':source.name,'category':category,'target':target,'path':path}
                individual.append(record)
                dest=REPO/path
            else:
                existing=REPO/'collections/video-paper-workflow'/source.name
                if existing.is_dir() and inventory(existing)==inv:
                    path=existing.relative_to(REPO).as_posix()
                else:
                    path=f'collections/installed-packages/{source.name}'
                record={'name':source.name,'category':'career-job-search' if source.name=='asu-skills' else 'academic-research','target':target,'path':path,'skillCount':len(skillpaths)}
                if source.name=='asu-skills':
                    record.update(source='https://github.com/Hisn00w/ASu-skills',commit='d27fd2a3864c48472a5c8ed942410098ba9cd35f',license='MIT')
                packages.append(record)
                dest=REPO/path
            rows.append((source,dest,inv))
            for rel in skillpaths:
                content=(source/rel).read_text(encoding='utf-8-sig',errors='replace')
                found=re.search(r'^name:\s*[\"\x27]?([^\r\n\"\x27]+)',content,re.M)
                name=found.group(1).strip() if found else Path(rel).parent.name or source.name
                duplicates[name].append({'target':target,'package':source.name,'path':rel,'sha256':inv[rel]})
    if issues:
        raise SystemExit('Potential live credentials require review (values withheld): '+json.dumps(issues,ensure_ascii=False))
    for source,dest,inv in rows:
        copy_snapshot(source,dest,inv)
    manifest.update(schema=2,updated='2026-10-31',skills=individual,packages=packages)
    (REPO/'skills-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    audit={'updated':'2026-10-31','hashPolicy':'SHA256; UTF-8 text without NUL normalizes CRLF to LF; binary files use raw bytes','standaloneCount':len(individual),'packageCount':len(packages),'skillFileCount':sum(len([p for p in inv if p=='SKILL.md' or p.endswith('/SKILL.md')]) for _,_,inv in rows),
           'packages':[dict(name=x['name'],path=x['path'],skillCount=x['skillCount']) for x in packages],
           'duplicates':{name:entries for name,entries in sorted(duplicates.items()) if len(entries)>1},
           'files':[{ 'path':dest.relative_to(REPO).as_posix()+'/'+rel,'sha256':digest} for _,dest,inv in rows for rel,digest in inv.items()]}
    (REPO/'inventory.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    catalog=['# Installed skill catalog','',f"Snapshot: 2026-10-31. {len(individual)} standalone skills and {len(packages)} packages; {audit['skillFileCount']} SKILL.md files.",'','## Standalone skills','']
    for category in sorted({x['category'] for x in individual}):
        catalog.extend(['### '+category,''])
        catalog.extend(f"- [{x['name']}]({x['path']}/SKILL.md) ({x['target']})" for x in individual if x['category']==category)
        catalog.append('')
    catalog.extend(['## Complete packages','','| Package | SKILL.md files | Archive |','| --- | ---: | --- |'])
    catalog.extend(f"| {x['name']} | {x['skillCount']} | [{x['path']}]({x['path']}) |" for x in packages)
    catalog.extend(['','## Repeated skill names','',f"{len(audit['duplicates'])} names occur in multiple packages or variants. Entries retain their original directory and provenance; no active local skills were deleted. See inventory.json for the paths and hashes. Identical pre-existing collection packages are referenced, not copied again.",'','System skills and plugin caches are excluded. Existing historical collections remain available but are only restored when listed in skills-manifest.json.',''])
    (REPO/'CATALOG.md').write_text('\n'.join(catalog),encoding='utf-8')
    print(json.dumps({k:audit[k] for k in ['standaloneCount','packageCount','skillFileCount']},ensure_ascii=False))
    print('Duplicate names retained with package provenance: '+str(len(audit['duplicates'])))
    print('Archived files: '+str(len(audit['files'])))

if __name__=='__main__':
    main()
