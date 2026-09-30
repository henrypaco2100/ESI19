from pathlib import Path
import ast
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
errors = []
mods = [p for p in root.iterdir() if p.is_dir() and (p/'__manifest__.py').exists()]
for mod in sorted(mods):
    try:
        text=(mod/'__manifest__.py').read_text(encoding='utf-8')
        data=ast.literal_eval(text[text.find('{'):])
        assert str(data.get('version','')).startswith('19.0.')
        assert data.get('installable') is True
    except Exception as e:
        errors.append(f'{mod.name}: manifest: {e}')
    for xml in mod.rglob('*.xml'):
        try:
            ET.parse(xml)
        except Exception as e:
            errors.append(f'{xml}: XML: {e}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'OK: {len(mods)} modulos; manifests y XML validos.')
