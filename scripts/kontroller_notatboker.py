"""Kontroller kursnotatbøker, og kjør eventuelt løsninger fra nye kjerner."""

import argparse
import ast
from pathlib import Path
from time import perf_counter

import nbformat
from nbclient import NotebookClient


ROT = Path(__file__).resolve().parent.parent


def kontroller():
    oppgaver = sorted((ROT / "oppgaver").glob("*.ipynb"))
    losninger = sorted((ROT / "solutions").glob("*.ipynb"))
    assert len(oppgaver) == 5, "Forventet fem oppgavenotatbøker."
    assert [fil.name for fil in oppgaver] == [fil.name for fil in losninger]
    antall_oppgaver = 0
    antall_svar = 0
    for oppgavefil, losningsfil in zip(oppgaver, losninger):
        oppgave = nbformat.read(oppgavefil, as_version=4)
        losning = nbformat.read(losningsfil, as_version=4)
        nbformat.validate(oppgave)
        nbformat.validate(losning)
        assert len(oppgave.cells) == len(losning.cells)
        for studentcelle, losningscelle in zip(oppgave.cells, losning.cells):
            assert studentcelle.cell_type == losningscelle.cell_type
            assert studentcelle.metadata == losningscelle.metadata
            assert studentcelle.id == losningscelle.id
            rolle = studentcelle.metadata.get("kursrolle")
            if rolle == "oppgave":
                antall_oppgaver += 1
                assert studentcelle.cell_type == "code"
                assert not ast.parse(studentcelle.source).body, "Oppgavecellen skal være tom for kode."
                assert ast.parse(losningscelle.source).body, "Løsningen mangler kode."
            elif rolle == "svar":
                antall_svar += 1
                assert studentcelle.cell_type == "markdown"
                assert studentcelle.source.startswith("**Mitt svar:**")
                assert losningscelle.source.startswith("**Mitt svar:**")
                assert "..." not in losningscelle.source, "Løsningen mangler et skriftlig svar."
                assert studentcelle.source != losningscelle.source
            else:
                assert studentcelle.source == losningscelle.source, "Felles undervisningsinnhold avviker."
            for celle in (studentcelle, losningscelle):
                if celle.cell_type == "code":
                    ast.parse(celle.source, filename=oppgavefil.name)
                    assert celle.execution_count is None, "Innsjekkede notatbøker skal være uten kjøredata."
                    assert not celle.outputs, "Kjøredata skal bare ligge i outputs/."
        print(f"Kontrollert: {oppgavefil.name}", flush=True)
    print(f"Totalt: {antall_oppgaver} kodeoppgaver og {antall_svar} skriftlige svaroppgaver.", flush=True)
    return losninger


def kjor(losninger):
    utdatamappe = ROT / "outputs" / "solutions"
    utdatamappe.mkdir(parents=True, exist_ok=True)
    for fil in losninger:
        notatbok = nbformat.read(fil, as_version=4)
        start = perf_counter()
        print(f"Kjører {fil.name} …", flush=True)
        klient = NotebookClient(
            notatbok,
            timeout=300,
            kernel_name="python3",
            resources={"metadata": {"path": str(fil.parent)}},
        )
        klient.execute()
        nbformat.write(notatbok, utdatamappe / fil.name)
        figurer = sum(
            "image/png" in resultat.get("data", {})
            for celle in notatbok.cells if celle.cell_type == "code"
            for resultat in celle.outputs
        )
        print(f"Fullført på {perf_counter() - start:.1f} s; {figurer} figurer.", flush=True)
        # Vis tall fra kjøringen uten å skrive ut bildedata.
        for celle in notatbok.cells:
            for resultat in celle.get("outputs", []):
                if resultat.output_type == "stream":
                    print(resultat.text.rstrip(), flush=True)
    print(f"Kjørte kopier ligger i {utdatamappe.relative_to(ROT)}.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kjor", action="store_true", help="Kjør alle løsninger og lagre kopier med resultater.")
    argumenter = parser.parse_args()
    filer = kontroller()
    if argumenter.kjor:
        kjor(filer)
