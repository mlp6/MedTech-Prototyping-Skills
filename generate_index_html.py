from pathlib import Path
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

with open('index.html', 'w') as f:

    index_header = """
        <!doctype html>
        <html>
        <head>
          <title>MedTech Prototyping Skills Resources</title>
        </head>

        <body>
    """
    f.write(index_header)

    f.write('<h1>MedTech Prototyping Skills (BME290L) Resources</h1>\n')

    f.write(f'<p>This index and these PDF files are auto-compiled ({now} UTC) '
            'from the GitLab CI runner associated with this repository.</p>\n')

    f.write('<h2>Syllabus</h2>\n')
    syllabus = 'Prototyping-S23-Syllabus-Palmeri.pdf'
    f.write(f'<a href="{syllabus}">{syllabus}</a>\n')

    f.write('<h2>Lectures</h2>\n')
    f.write('<ol>\n')
    for lecture in sorted(list(Path('lectures').rglob('*.pdf'))):
        f.write(f'<li><a href="{lecture.name}">{lecture.name}</a></li>\n')
    f.write('</ol>\n')

    f.write('<h2>Labs</h2>\n')
    f.write('<ol>\n')
    for lab in sorted(list(Path('labs').rglob('Prototyping-*.pdf'))):
        f.write(f'<li><a href="{lab.name}">{lab.name}</a></li>\n')
    f.write('</ol>\n')

    f.write('<h2>Resources</h2>\n')
    f.write('<ol>\n')
    for r in sorted(list(Path('resources').rglob('*.pdf'))):
        f.write(f'<li><a href="{r.name}">{r.name}</a></li>\n')
    f.write('</ol>\n')
    f.write('</body>\n')

    f.write('<footer>\n')

    f.write('<p>&copy; 2023 Mark Palmeri (Duke University)</p>\n')

    license = """
        <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img
        alt="Creative Commons License" style="border-width:0"
        src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This
        work is licensed under a <a rel="license"
        href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons
        Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
    """
    f.write(license)

    f.write('</footer>\n')

    f.write('</html>\n')
