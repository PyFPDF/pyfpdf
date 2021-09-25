[![build status](https://github.com/PyFPDF/fpdf2/workflows/build/badge.svg)](https://github.com/PyFPDF/fpdf2/actions?query=branch%3Amaster)
[![Pypi latest version](https://img.shields.io/pypi/v/fpdf2.svg)](https://pypi.python.org/pypi/fpdf2)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![codecov](https://codecov.io/gh/PyFPDF/fpdf2/branch/master/graph/badge.svg)](https://codecov.io/gh/PyFPDF/fpdf2)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Downloads per month](https://pepy.tech/badge/fpdf2/month)](https://pepy.tech/project/fpdf2)

[![Discussions](https://img.shields.io/github/discussions/PyFPDF/fpdf2)](https://github.com/PyFPDF/fpdf2/discussions)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![first-timers-only Friendly](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)
-> come look at our [good first issues](https://github.com/PyFPDF/fpdf2/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

fpdf2
=====

![fpdf2 logo](https://pyfpdf.github.io/fpdf2/fpdf2-logo.png)

`fpdf2` is a PDF creation library for Python:

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(txt="hello world")
pdf.output("hello_world.pdf")
```

It is a fork and the successor of `PyFPDF` (_cf._ [history](https://pyfpdf.github.io/fpdf2/Development.html#history)).
Compared with other PDF libraries, `fpdf2` is **fast, versatile, easy to learn and to extend** ([example](https://github.com/digidigital/Extensions-and-Scripts-for-pyFPDF-fpdf2)).
It is also entirely writen in Python and only has a couple of dependencies:
[Pillow](https://pillow.readthedocs.io/en/stable/) & [defusedxml](https://pypi.org/project/defusedxml/).

**Development status**: this project is **mature** and **actively maintained**.

We are looking for contributing developers: if you want to get involved but don't know how,
or would like to volunteer helping maintain this lib, [open a discussion](https://github.com/PyFPDF/fpdf2/discussions)!

Installation Instructions
-------------------------
```bash
pip install fpdf2
```

To get the latest, unreleased, development version straight from the development branch of this repository:

```bash
pip install git+https://github.com/PyFPDF/fpdf2.git@master
```

Features
--------

 * Python 3.6+ support
 * [Unicode](https://pyfpdf.github.io/fpdf2/Unicode.html) (UTF-8) TrueType font subset embedding
 * Internal / external [links](https://pyfpdf.github.io/fpdf2/Links.html)
 * Embedding images, including transparency and alpha channel
 * Arbitrary path drawing and basic [SVG](https://pyfpdf.github.io/fpdf2/SVG.html) import
 * Embedding [barcodes](https://pyfpdf.github.io/fpdf2/Barcodes.html), [charts & graphs](https://pyfpdf.github.io/fpdf2/Maths.html), [emojis, symbols & dingbats](https://pyfpdf.github.io/fpdf2/EmojisSymbolsDingbats.html)
 * [Cell / multi-cell / plaintext writing](https://pyfpdf.github.io/fpdf2/Text.html), with [automatic page breaks](https://pyfpdf.github.io/fpdf2/PageBreaks.html), line break and text justification
 * Choice of measurement unit, page format & margins. Optional page header and footer
 * Basic [conversion from HTML to PDF](https://pyfpdf.github.io/fpdf2/HTML.html)
 * A [templating system](https://pyfpdf.github.io/fpdf2/Templates.html) to render PDFs in batchs
 * Images & links alternative descriptions, for accessibility
 * Table of contents & [document outline](https://pyfpdf.github.io/fpdf2/DocumentOutlineAndTableOfContents.html)
 * [Annotations](https://pyfpdf.github.io/fpdf2/Annotations.html), including text highlights
 * [Presentation mode](https://pyfpdf.github.io/fpdf2/Presentations.html) with control over page display duration & transitions
 * Unit tests with `qpdf`-based PDF diffing and a high code coverage
 * Optional basic Markdown-like styling: `**bold**, __italics__`
 * Can render [mathematical equations & charts](https://pyfpdf.github.io/fpdf2/Maths.html)
 * Usage examples with [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com), [streamlit](https://streamlit.io/), AWS lambdas... : [Usage in web APIs](https://pyfpdf.github.io/fpdf2/UsageInWebAPI.html)

Our 300+ reference PDF test files, generated by `fpdf2`, are validated using 3 different checkers:

[![QPDF logo](https://pyfpdf.github.io/fpdf2/qpdf-logo.svg)](https://github.com/qpdf/qpdf)
[![PDF Checker logo](https://pyfpdf.github.io/fpdf2/pdfchecker-logo.png)](https://www.datalogics.com/products/pdf-tools/pdf-checker/)
[![VeraPDF logo](https://pyfpdf.github.io/fpdf2/vera-logo.jpg)](https://verapdf.org)

Documentation
-------------

- [Documentation Home](https://pyfpdf.github.io/fpdf2/)
- Tutorial in several languages: [English](https://pyfpdf.github.io/fpdf2/Tutorial.html) - [Deutsch](https://pyfpdf.github.io/fpdf2/Tutorial-de.html) - [español](https://pyfpdf.github.io/fpdf2/Tutorial-es.html) - [हिंदी](https://pyfpdf.github.io/fpdf2/Tutorial-हिंदी.html) [português](https://pyfpdf.github.io/fpdf2/Tutorial-pt.html) - [Русский](https://pyfpdf.github.io/fpdf2/Tutorial-ru.html) - [Italian](https://pyfpdf.github.io/fpdf2/Tutorial-it.html) - [français](https://pyfpdf.github.io/fpdf2/Tutorial-fr.html)
- Release notes: [CHANGELOG.md](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md)
- A series of blog posts: [fpdf2 tag @ ludochaordic](https://chezsoi.org/lucas/blog/tag/fpdf2.html)

You can also have a look at the `tests/`, they're great usage examples!

Developement
------------

Please check the [dedicated documentation page](https://pyfpdf.github.io/fpdf2/Development.html).

## Contributors ✨

This library could only exist thanks to the dedication of many volunteers around the world:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/reingart"><img src="https://avatars.githubusercontent.com/u/1041385?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mariano Reingart</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=reingart" title="Code">💻</a></td>
    <td align="center"><a href="http://lymaconsulting.github.io/"><img src="https://avatars.githubusercontent.com/u/8921892?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David Ankin</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Aalexanderankin" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexanderankin" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexanderankin" title="Documentation">📖</a> <a href="#maintenance-alexanderankin" title="Maintenance">🚧</a> <a href="#question-alexanderankin" title="Answering Questions">💬</a> <a href="https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+reviewed-by%3Aalexanderankin" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexanderankin" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/alexp1917"><img src="https://avatars.githubusercontent.com/u/66129071?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alex Pavlovich</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Aalexp1917" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexp1917" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexp1917" title="Documentation">📖</a> <a href="#question-alexp1917" title="Answering Questions">💬</a> <a href="https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+reviewed-by%3Aalexp1917" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=alexp1917" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://chezsoi.org/lucas/blog/"><img src="https://avatars.githubusercontent.com/u/925560?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lucas Cimon</b></sub></a><br /><a href="#blog-Lucas-C" title="Blogposts">📝</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=Lucas-C" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=Lucas-C" title="Documentation">📖</a> <a href="#infra-Lucas-C" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-Lucas-C" title="Maintenance">🚧</a> <a href="#question-Lucas-C" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/eumiro"><img src="https://avatars.githubusercontent.com/u/6774676?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Miroslav Šedivý</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=eumiro" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=eumiro" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/fbernhart"><img src="https://avatars.githubusercontent.com/u/70264417?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Florian Bernhart</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=fbernhart" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=fbernhart" title="Tests">⚠️</a></td>
    <td align="center"><a href="http://pr.linkedin.com/in/edwoodocasio/"><img src="https://avatars.githubusercontent.com/u/82513?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Edwood Ocasio</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=eocasio" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=eocasio" title="Tests">⚠️</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/marcelotduarte"><img src="https://avatars.githubusercontent.com/u/12752334?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marcelo Duarte</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=marcelotduarte" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/RomanKharin"><img src="https://avatars.githubusercontent.com/u/6203756?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Roman Kharin</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=RomanKharin" title="Code">💻</a> <a href="#ideas-RomanKharin" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/cgfrost"><img src="https://avatars.githubusercontent.com/u/166104?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christopher Frost</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Acgfrost" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=cgfrost" title="Code">💻</a></td>
    <td align="center"><a href="http://www.ne.ch/sitn"><img src="https://avatars.githubusercontent.com/u/1681332?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael Kalbermatten</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Akalbermattenm" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=kalbermattenm" title="Code">💻</a></td>
    <td align="center"><a href="https://yanone.de/"><img src="https://avatars.githubusercontent.com/u/175386?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yanone</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=yanone" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/leoleozhu"><img src="https://avatars.githubusercontent.com/u/738445?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Leo Zhu</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=leoleozhu" title="Code">💻</a></td>
    <td align="center"><a href="https://www.abishekgoda.com/"><img src="https://avatars.githubusercontent.com/u/310520?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abishek Goda</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=abishek" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.cd-net.net/"><img src="https://avatars.githubusercontent.com/u/1515637?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Arthur Moore</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=EmperorArthur" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=EmperorArthur" title="Tests">⚠️</a> <a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3AEmperorArthur" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://boghison.com/"><img src="https://avatars.githubusercontent.com/u/7976283?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bogdan Cuza</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=boghison" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/craigahobbs"><img src="https://avatars.githubusercontent.com/u/1263515?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Craig Hobbs</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=craigahobbs" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/xitrushiy"><img src="https://avatars.githubusercontent.com/u/17336659?v=4?s=100" width="100px;" alt=""/><br /><sub><b>xitrushiy</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Axitrushiy" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=xitrushiy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jredrejo"><img src="https://avatars.githubusercontent.com/u/1008178?v=4?s=100" width="100px;" alt=""/><br /><sub><b>José L. Redrejo Rodríguez</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=jredrejo" title="Code">💻</a></td>
    <td align="center"><a href="https://jugmac00.github.io/"><img src="https://avatars.githubusercontent.com/u/9895620?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jürgen Gmach</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=jugmac00" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Larivact"><img src="https://avatars.githubusercontent.com/u/8731884?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Larivact</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=Larivact" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/leonelcamara"><img src="https://avatars.githubusercontent.com/u/1198145?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Leonel Câmara</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=leonelcamara" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mark-steadman"><img src="https://avatars.githubusercontent.com/u/15779053?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mark Steadman</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Amark-steadman" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=mark-steadman" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sergeyfitts"><img src="https://avatars.githubusercontent.com/u/40498252?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sergey</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=sergeyfitts" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Stan-C421"><img src="https://avatars.githubusercontent.com/u/82440217?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Stan-C421</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=Stan-C421" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/viraj-shah18"><img src="https://avatars.githubusercontent.com/u/44942391?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Viraj Shah</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=viraj-shah18" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/cornicis"><img src="https://avatars.githubusercontent.com/u/11545033?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cornicis</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=cornicis" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/moe-25"><img src="https://avatars.githubusercontent.com/u/85580959?v=4?s=100" width="100px;" alt=""/><br /><sub><b>moe-25</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=moe-25" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+reviewed-by%3Amoe-25" title="Reviewed Pull Requests">👀</a> <a href="#research-moe-25" title="Research">🔬</a> <a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Amoe-25" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/niphlod"><img src="https://avatars.githubusercontent.com/u/122119?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Simone Bizzotto</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=niphlod" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/bnyw"><img src="https://avatars.githubusercontent.com/u/32655514?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Boonyawe Sirimaha</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Abnyw" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/torque"><img src="https://avatars.githubusercontent.com/u/949138?v=4?s=100" width="100px;" alt=""/><br /><sub><b>T</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=torque" title="Code">💻</a> <a href="#design-torque" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/AubsUK"><img src="https://avatars.githubusercontent.com/u/68870168?v=4?s=100" width="100px;" alt=""/><br /><sub><b>AubsUK</b></sub></a><br /><a href="#question-AubsUK" title="Answering Questions">💬</a></td>
    <td align="center"><a href="http://www.schorsch.com/"><img src="https://avatars.githubusercontent.com/u/17468844?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Georg Mischler</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Agmischler" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=gmischler" title="Code">💻</a> <a href="#design-gmischler" title="Design">🎨</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=gmischler" title="Documentation">📖</a> <a href="#ideas-gmischler" title="Ideas, Planning, & Feedback">🤔</a> <a href="#question-gmischler" title="Answering Questions">💬</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=gmischler" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://www.buymeacoffee.com/ping"><img src="https://avatars.githubusercontent.com/u/104607?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ping</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Aping" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://portfedh@gmail.com"><img src="https://avatars.githubusercontent.com/u/59422723?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Portfedh</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=portfedh" title="Documentation">📖</a> <a href="#tutorial-portfedh" title="Tutorials">✅</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/tabarnhack"><img src="https://avatars.githubusercontent.com/u/34366899?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tabarnhack</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=tabarnhack" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Mridulbirla13"><img src="https://avatars.githubusercontent.com/u/24730417?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mridul Birla</b></sub></a><br /><a href="#translation-Mridulbirla13" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/digidigital"><img src="https://avatars.githubusercontent.com/u/28964886?v=4?s=100" width="100px;" alt=""/><br /><sub><b>digidigital</b></sub></a><br /><a href="#translation-digidigital" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/xit4"><img src="https://avatars.githubusercontent.com/u/7601720?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Xit</b></sub></a><br /><a href="#translation-xit4" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/AABur"><img src="https://avatars.githubusercontent.com/u/41373199?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Burchenko</b></sub></a><br /><a href="#translation-AABur" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/fuscati"><img src="https://avatars.githubusercontent.com/u/48717599?v=4?s=100" width="100px;" alt=""/><br /><sub><b>André Assunção</b></sub></a><br /><a href="#translation-fuscati" title="Translation">🌍</a></td>
    <td align="center"><a href="http://frenchcomputerguy.com/"><img src="https://avatars.githubusercontent.com/u/5825096?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Quentin Brault</b></sub></a><br /><a href="#translation-Tititesouris" title="Translation">🌍</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/paulacampigotto"><img src="https://avatars.githubusercontent.com/u/36995920?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Paula Campigotto</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Apaulacampigotto" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=paulacampigotto" title="Code">💻</a> <a href="https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+reviewed-by%3Apaulacampigotto" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/bettman-latin"><img src="https://avatars.githubusercontent.com/u/91155492?v=4?s=100" width="100px;" alt=""/><br /><sub><b>bettman-latin</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=bettman-latin" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/oleksii-shyman"><img src="https://avatars.githubusercontent.com/u/8827452?v=4?s=100" width="100px;" alt=""/><br /><sub><b>oleksii-shyman</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=oleksii-shyman" title="Code">💻</a> <a href="#design-oleksii-shyman" title="Design">🎨</a> <a href="#ideas-oleksii-shyman" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://lcomrade.su"><img src="https://avatars.githubusercontent.com/u/70049256?v=4?s=100" width="100px;" alt=""/><br /><sub><b>lcomrade</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=lcomrade" title="Documentation">📖</a> <a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Alcomrade" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=lcomrade" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/pwt"><img src="https://avatars.githubusercontent.com/u/1089749?v=4?s=100" width="100px;" alt=""/><br /><sub><b>pwt</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Apwt" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=pwt" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mcerveny"><img src="https://avatars.githubusercontent.com/u/1438115?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Martin Cerveny</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Amcerveny" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/commits?author=mcerveny" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Spenhouet"><img src="https://avatars.githubusercontent.com/u/7819068?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Spenhouet</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3ASpenhouet" title="Bug reports">🐛</a> <a href="https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+reviewed-by%3ASpenhouet" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/mtkumar123"><img src="https://avatars.githubusercontent.com/u/89176219?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mtkumar123</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=mtkumar123" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/RedShy"><img src="https://avatars.githubusercontent.com/u/24901693?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Davide Consalvo</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=RedShy" title="Code">💻</a></td>
    <td align="center"><a href="http://blog.whatgeek.com.pt"><img src="https://avatars.githubusercontent.com/u/2813722?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bruno Santos</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/issues?q=author%3Afeiticeir0" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/cgkoutzigiannis"><img src="https://avatars.githubusercontent.com/u/41803093?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cgkoutzigiannis</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=cgkoutzigiannis" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/iwayankurniawan"><img src="https://avatars.githubusercontent.com/u/30134645?v=4?s=100" width="100px;" alt=""/><br /><sub><b>I Wayan Kurniawan</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=iwayankurniawan" title="Documentation">📖</a></td>
    <td align="center"><a href="https://rysta.io"><img src="https://avatars.githubusercontent.com/u/4029642?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sven Eliasson</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=comino" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/gonzalobarbaran"><img src="https://avatars.githubusercontent.com/u/59395855?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gonzalobarbaran</b></sub></a><br /><a href="https://github.com/PyFPDF/fpdf2/commits?author=gonzalobarbaran" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification
([emoji key](https://allcontributors.org/docs/en/emoji-key)).
Contributions of any kind welcome!

[![Contributors map](https://pyfpdf.github.io/fpdf2/contributors-map-small.png)](https://pyfpdf.github.io/fpdf2/contributors.html)

_(screenshot from June 2021, click on the map above to access an up-to-date online version)_

Community, related tools, alternative libraries
-----------------------------------------------

More about those in [the documentation](https://pyfpdf.github.io/fpdf2/#community).