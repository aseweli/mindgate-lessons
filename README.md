# MindGate lessons

Lessons and WeBWorK-style practice problems for the MindGate study app (`aseweli/mindgate`): MATH 1451 and CHEM 1307,
Texas Tech, Fall 2026. The app downloads this repository (Settings → Pull questions, and automatically every 2 hours while
it's open) and keeps a copy on the Mac for offline study.

- **How to write lessons and problems:** [AUTHORING.md](AUTHORING.md)
- Course structure, exam dates and textbook exercise lists: `courses/<course>/course.json`
- Check before pushing: `python3 tools/check_content.py ../mindgate-lessons` from the app repo (must print `RESULT: ALL OK`)
