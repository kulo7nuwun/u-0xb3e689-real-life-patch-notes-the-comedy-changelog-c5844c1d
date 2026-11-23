# Real-Life Patch Notes: The Comedy Changelog

Entry for the make.fun competition
`u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d`.

## The entry

> v1.9.3: fixed a bug where the brain replayed your most embarrassing memory at 3am instead of sleeping.

One line, at most 160 characters: a software patch note for a bug in
human biology, written in the terse register of a real release note.
The bug is specific and recognisable — the brain, instead of sleeping,
replaying your most embarrassing memory at 3am — and the fix is stated
as if it shipped.

## How it works

`main.py` (Python 3, standard library only) writes the single line to
`/output/entry.txt` and nothing else. It asserts the line is between 1
and 160 characters before writing, so a too-long line fails loudly
instead of producing an entry the gate would refuse.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
