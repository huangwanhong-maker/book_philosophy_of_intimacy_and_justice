# CITATION_RESOLUTIONS

> Verified bibliographic data for the contested keys flagged in
> [`CITATION_AUDIT.md`](CITATION_AUDIT.md). Each was checked against an
> authoritative source (publisher/journal/DOI/archive) with the URL recorded.
> These replace the `>> PROVISIONAL <<` entries in `bib/master.bib`.
>
> Verified 2026-07 via web sources. The corresponding source `refs.bib`
> entries are being corrected; `master.bib` is then regenerated.

## Externally verified (source-confirmed)

| Key | Resolution | Source |
|-----|-----------|--------|
| `eglash2016` | *An Introduction to Generative Justice*, **Teknokultura 13(2):369–404**, 2016. DOI `10.5209/rev_TEKN.2016.v13.n2.52847`. (The `369–388` in papers IX–XXIII is **wrong**.) | revistas.ucm.es/…/52847 |
| `eglash2016generative` | **Separate article** — *Of Marx and Makers: An Historical Perspective on Generative Justice*, **Teknokultura 13(1):245–269**, 2016. DOI `10.5209/rev_TK.2016.v13.n1.52096`. Must be split from `eglash2016`; paper I cites this one. | revistas.ucm.es/…/52096 |
| `sartre1943` | Sartre, *Being and Nothingness*, trans. **Hazel E. Barnes**; French orig. *L'Être et le néant* (Gallimard, **origyear 1943**). Standard English: **Philosophical Library, 1956**; Washington Square reprints (1966/1984) are the same Barnes text. | en.wikipedia.org/wiki/Being_and_Nothingness |
| `lacan1977xi` | *The Four Fundamental Concepts of Psychoanalysis* (**Seminar XI**), trans. **Alan Sheridan**, ed. Miller. **Norton, 1978** (US, standard) / Hogarth 1977 (UK). | en.wikipedia.org/…/The_Four_Fundamental_Concepts… |
| `lacan1992` / `lacan1992vii` | *The Ethics of Psychoanalysis 1959–1960* (**Seminar VII**), trans. **Dennis Porter**, ed. Miller. **Norton, 1992** (US, standard); Routledge 1992 (UK). | routledge.com / pep-web.org |
| `lacan1998` | *On Feminine Sexuality… Encore* (**Seminar XX**, 1972–73), trans. **Bruce Fink**, ed. Miller. **Norton, 1998**. (Paper V mislabels this as Seminar XI — see split below.) | amazon/philpapers LACOFS |
| `hobbes1651` | *Leviathan*, ed. **Richard Tuck**, Cambridge Texts in the History of Political Thought, **CUP, rev. student edn 1996** (first Tuck 1991). **origyear 1651**. | CUP 0521567971 |
| `nussbaum2001` → split | **(a)** *The Fragility of Goodness*, **CUP 1986** (rev. 2001), origyear 1986 — cited by XI, XIII. **(b)** *Women and Human Development: The Capabilities Approach*, **CUP 2000** — cited by XVIII–XXIII. | cambridge.org (both) |
| `geertz1973` | `@incollection` — *Thick Description: Toward an Interpretive Theory of Culture*, in *The Interpretation of Cultures*, **Basic Books, 1973, pp. 3–30**. | archive.org interpretationof00geer |
| `berry1984` | M. V. Berry, *Quantal phase factors accompanying adiabatic changes*, **Proc. R. Soc. Lond. A 392(1802):45–57**, 1984. DOI `10.1098/rspa.1984.0023`. (Not 45–47.) | royalsocietypublishing.org |
| `trevarthen1979` | `@incollection` — *Communication and cooperation in early infancy: A description of primary intersubjectivity*, in M. Bullowa (ed.), *Before Speech*, **CUP, 1979, pp. 321–347**. | philpapers TRECAC-2 |
| `simmel1950` | *The Sociology of Georg Simmel*, ed./trans. **Kurt H. Wolff**, **Free Press, 1950**. "Quantitative Aspects of the Group" = Part Two (≈ pp. 87–177 — **page span UNCONFIRMED**, verify against a copy). | archive.org sociologyofgeorg |
| `marx1867capital` | *Capital, Vol. I*, trans. **Ben Fowkes**, **Penguin/New Left Review, 1976** (Vintage 1977). **origyear 1867**. | penguin 0140445684 |
| `legge1963yijing` | trans. **James Legge**, *The I Ching: The Book of Changes*, **Dover, 1963** (reprint of 1899 Sacred Books of the East XVI). origyear 1899. | doverpublications |
| `saussure1916course` | Saussure, Ferdinand de (sort **Saussure**), *Course in General Linguistics*, trans. **Wade Baskin**, **Philosophical Library, 1959**. **origyear 1916**. | jstor 10.7312/saus15726 |
| `zizek1989sublime` | **Slavoj Žižek**, *The Sublime Object of Ideology*, **Verso, 1989**. (Fix the mangled `v ziv zek` encoding.) | versobooks.com |

## Key collisions requiring a split (one key → two works)

| Old key | Becomes |
|---------|---------|
| `eglash2016generative` | keep for *Of Marx and Makers* (13(1)); paper I already uses it correctly. Ensure `eglash2016` = the *Introduction* (13(2)). |
| `nussbaum2001` | `nussbaum1986fragility` (Fragility) + `nussbaum2000women` (Women & Human Development); rewrite each citing paper to the right one. |
| `lacan1998` | in paper V it points to Seminar XI (should be `lacan1977xi`); elsewhere it is Encore/Seminar XX. Repoint paper V. |
| `geertz1973`, `simmel1950` | resolve `@book` vs `@incollection` to the incollection forms above. |

## Still author-authoritative (from each paper's own cover, not external)

- `paperix`, `paperxiii`, `paperxv` self-citations and `wan2024grb` year — reconcile
  against each paper's own title block when revising Volumes II–III (they are not
  cited within Volume I). See [`CITATION_AUDIT.md`](CITATION_AUDIT.md) §B.
