"""Restore standalone skills and complete packages, preserving overwritten folders."""
import argparse
import datetime
import hashlib
import json
import shutil
from pathlib import Path

def digest_file(path):
    data=path.read_bytes()
    try:
        data.decode('utf-8')
        if b'\0' not in data:
            data=data.replace(b'\r\n',b'\n')
    except UnicodeDecodeError:
        pass
    return hashlib.sha256(data).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--force',action='store_true')
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--only',action='append',default=[])
    parser.add_argument('--home',type=Path,default=Path.home())
    parser.add_argument('--check',action='store_true',help='Verify archived file hashes; do not install')
    args=parser.parse_args()
    repo=Path(__file__).resolve().parents[1]
    manifest=json.loads((repo/'skills-manifest.json').read_text(encoding='utf-8-sig'))
    if args.check:
        inventory=json.loads((repo/'inventory.json').read_text(encoding='utf-8'))
        failures=[]
        for row in inventory['files']:
            p=repo/row['path']
            if not p.is_file() or digest_file(p)!=row['sha256']:
                failures.append(row['path'])
        if failures:
            raise SystemExit('Archive mismatch: '+json.dumps(failures))
        print(f"Verified {len(inventory['files'])} archived files")
        return
    records=manifest['skills']+manifest.get('packages',[])
    known={r['name'] for r in records}
    if set(args.only)-known:
        parser.error('Unknown selection: '+', '.join(sorted(set(args.only)-known)))
    stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    for item in records:
        if args.only and item['name'] not in args.only:
            continue
        name=item['name']
        if Path(name).name!=name or name in {'.','..','.system'} or item['target'] not in {'agents','codex'}:
            raise SystemExit('Invalid restore target: '+name)
        source=(repo/item['path']).resolve()
        if not source.is_relative_to(repo) or not source.is_dir() or not list(source.rglob('SKILL.md')):
            raise SystemExit('Invalid archive source: '+item['path'])
        base=(args.home/('.codex' if item['target']=='codex' else '.agents')/'skills').resolve()
        destination=base/name
        if destination.exists() and not args.force:
            print('Skip existing: '+name)
            continue
        if args.dry_run:
            print('Would restore: '+item['target']+'/'+name)
            continue
        base.mkdir(parents=True,exist_ok=True)
        if destination.exists():
            backup=args.home/'.codex'/'skill-backups'/stamp/item['target']/name
            backup.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(destination),str(backup))
            print('Previous version backed up: '+str(backup))
        shutil.copytree(source,destination)
        print('Restored: '+name)
    print('Done. Skills will be available on the next turn; refresh or start a new chat if needed.')


if __name__=='__main__':
    main()
