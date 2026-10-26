# agent-issue-test

A small demo repository used to exercise an automated
`issue -> triage -> code -> test -> deliver` agent pipeline.

## Layout

- `src/calc.py` — arithmetic helpers
- `src/textutil.py` — string helpers
- `tests/` — unittest suite

## Running the tests

```
python -m unittest discover -s tests -t . -v
```
