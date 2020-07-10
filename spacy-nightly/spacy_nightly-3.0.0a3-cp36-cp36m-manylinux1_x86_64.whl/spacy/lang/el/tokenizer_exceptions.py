from ...symbols import ORTH, LEMMA, NORM


_exc = {}

for token in ["Απ'", "ΑΠ'", "αφ'", "Αφ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "από", NORM: "από"}]

for token in ["Αλλ'", "αλλ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "αλλά", NORM: "αλλά"}]

for token in ["παρ'", "Παρ'", "ΠΑΡ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "παρά", NORM: "παρά"}]

for token in ["καθ'", "Καθ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "κάθε", NORM: "κάθε"}]

for token in ["κατ'", "Κατ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "κατά", NORM: "κατά"}]

for token in ["'ΣΟΥΝ", "'ναι", "'ταν", "'τανε", "'μαστε", "'μουνα", "'μουν"]:
    _exc[token] = [{ORTH: token, LEMMA: "είμαι", NORM: "είμαι"}]

for token in ["Επ'", "επ'", "εφ'", "Εφ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "επί", NORM: "επί"}]

for token in ["Δι'", "δι'"]:
    _exc[token] = [{ORTH: token, LEMMA: "δια", NORM: "δια"}]

for token in ["'χουν", "'χουμε", "'χαμε", "'χα", "'χε", "'χεις", "'χει"]:
    _exc[token] = [{ORTH: token, LEMMA: "έχω", NORM: "έχω"}]

for token in ["υπ'", "Υπ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "υπό", NORM: "υπό"}]

for token in ["Μετ'", "ΜΕΤ'", "'μετ"]:
    _exc[token] = [{ORTH: token, LEMMA: "μετά", NORM: "μετά"}]

for token in ["Μ'", "μ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "με", NORM: "με"}]

for token in ["Γι'", "ΓΙ'", "γι'"]:
    _exc[token] = [{ORTH: token, LEMMA: "για", NORM: "για"}]

for token in ["Σ'", "σ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "σε", NORM: "σε"}]

for token in ["Θ'", "θ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "θα", NORM: "θα"}]

for token in ["Ν'", "ν'"]:
    _exc[token] = [{ORTH: token, LEMMA: "να", NORM: "να"}]

for token in ["Τ'", "τ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "να", NORM: "να"}]

for token in ["'γω", "'σένα", "'μεις"]:
    _exc[token] = [{ORTH: token, LEMMA: "εγώ", NORM: "εγώ"}]

for token in ["Τ'", "τ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "το", NORM: "το"}]

for token in ["Φέρ'", "Φερ'", "φέρ'", "φερ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "φέρνω", NORM: "φέρνω"}]

for token in ["'ρθούνε", "'ρθουν", "'ρθει", "'ρθεί", "'ρθε", "'ρχεται"]:
    _exc[token] = [{ORTH: token, LEMMA: "έρχομαι", NORM: "έρχομαι"}]

for token in ["'πανε", "'λεγε", "'λεγαν", "'πε", "'λεγα"]:
    _exc[token] = [{ORTH: token, LEMMA: "λέγω", NORM: "λέγω"}]

for token in ["Πάρ'", "πάρ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "παίρνω", NORM: "παίρνω"}]

for token in ["μέσ'", "Μέσ'", "μεσ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "μέσα", NORM: "μέσα"}]

for token in ["Δέσ'", "Δεσ'", "δεσ'"]:
    _exc[token] = [{ORTH: token, LEMMA: "δένω", NORM: "δένω"}]

for token in ["'κανε", "Κάν'"]:
    _exc[token] = [{ORTH: token, LEMMA: "κάνω", NORM: "κάνω"}]

_other_exc = {
    "κι": [{ORTH: "κι", LEMMA: "και", NORM: "και"}],
    "Παίξ'": [{ORTH: "Παίξ'", LEMMA: "παίζω", NORM: "παίζω"}],
    "Αντ'": [{ORTH: "Αντ'", LEMMA: "αντί", NORM: "αντί"}],
    "ολ'": [{ORTH: "ολ'", LEMMA: "όλος", NORM: "όλος"}],
    "ύστερ'": [{ORTH: "ύστερ'", LEMMA: "ύστερα", NORM: "ύστερα"}],
    "'πρεπε": [{ORTH: "'πρεπε", LEMMA: "πρέπει", NORM: "πρέπει"}],
    "Δύσκολ'": [{ORTH: "Δύσκολ'", LEMMA: "δύσκολος", NORM: "δύσκολος"}],
    "'θελα": [{ORTH: "'θελα", LEMMA: "θέλω", NORM: "θέλω"}],
    "'γραφα": [{ORTH: "'γραφα", LEMMA: "γράφω", NORM: "γράφω"}],
    "'παιρνα": [{ORTH: "'παιρνα", LEMMA: "παίρνω", NORM: "παίρνω"}],
    "'δειξε": [{ORTH: "'δειξε", LEMMA: "δείχνω", NORM: "δείχνω"}],
    "όμουρφ'": [{ORTH: "όμουρφ'", LEMMA: "όμορφος", NORM: "όμορφος"}],
    "κ'τσή": [{ORTH: "κ'τσή", LEMMA: "κουτσός", NORM: "κουτσός"}],
    "μηδ'": [{ORTH: "μηδ'", LEMMA: "μήδε", NORM: "μήδε"}],
    "'ξομολογήθηκε": [
        {ORTH: "'ξομολογήθηκε", LEMMA: "εξομολογούμαι", NORM: "εξομολογούμαι"}
    ],
    "'μας": [{ORTH: "'μας", LEMMA: "εμάς", NORM: "εμάς"}],
    "'ξερες": [{ORTH: "'ξερες", LEMMA: "ξέρω", NORM: "ξέρω"}],
    "έφθασ'": [{ORTH: "έφθασ'", LEMMA: "φθάνω", NORM: "φθάνω"}],
    "εξ'": [{ORTH: "εξ'", LEMMA: "εκ", NORM: "εκ"}],
    "δώσ'": [{ORTH: "δώσ'", LEMMA: "δίνω", NORM: "δίνω"}],
    "τίποτ'": [{ORTH: "τίποτ'", LEMMA: "τίποτα", NORM: "τίποτα"}],
    "Λήξ'": [{ORTH: "Λήξ'", LEMMA: "λήγω", NORM: "λήγω"}],
    "άσ'": [{ORTH: "άσ'", LEMMA: "αφήνω", NORM: "αφήνω"}],
    "Στ'": [{ORTH: "Στ'", LEMMA: "στο", NORM: "στο"}],
    "Δωσ'": [{ORTH: "Δωσ'", LEMMA: "δίνω", NORM: "δίνω"}],
    "Βάψ'": [{ORTH: "Βάψ'", LEMMA: "βάφω", NORM: "βάφω"}],
    "Αλλ'": [{ORTH: "Αλλ'", LEMMA: "αλλά", NORM: "αλλά"}],
    "Αμ'": [{ORTH: "Αμ'", LEMMA: "άμα", NORM: "άμα"}],
    "Αγόρασ'": [{ORTH: "Αγόρασ'", LEMMA: "αγοράζω", NORM: "αγοράζω"}],
    "'φύγε": [{ORTH: "'φύγε", LEMMA: "φεύγω", NORM: "φεύγω"}],
    "'φερε": [{ORTH: "'φερε", LEMMA: "φέρνω", NORM: "φέρνω"}],
    "'φαγε": [{ORTH: "'φαγε", LEMMA: "τρώω", NORM: "τρώω"}],
    "'σπαγαν": [{ORTH: "'σπαγαν", LEMMA: "σπάω", NORM: "σπάω"}],
    "'σκασε": [{ORTH: "'σκασε", LEMMA: "σκάω", NORM: "σκάω"}],
    "'σβηνε": [{ORTH: "'σβηνε", LEMMA: "σβήνω", NORM: "σβήνω"}],
    "'ριξε": [{ORTH: "'ριξε", LEMMA: "ρίχνω", NORM: "ρίχνω"}],
    "'κλεβε": [{ORTH: "'κλεβε", LEMMA: "κλέβω", NORM: "κλέβω"}],
    "'κει": [{ORTH: "'κει", LEMMA: "εκεί", NORM: "εκεί"}],
    "'βλεπε": [{ORTH: "'βλεπε", LEMMA: "βλέπω", NORM: "βλέπω"}],
    "'βγαινε": [{ORTH: "'βγαινε", LEMMA: "βγαίνω", NORM: "βγαίνω"}],
}

_exc.update(_other_exc)

for h in range(1, 12 + 1):

    for period in ["π.μ.", "πμ"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, LEMMA: "π.μ.", NORM: "π.μ."},
        ]

    for period in ["μ.μ.", "μμ"]:
        _exc[f"{h}{period}"] = [
            {ORTH: f"{h}"},
            {ORTH: period, LEMMA: "μ.μ.", NORM: "μ.μ."},
        ]

for exc_data in [
    {ORTH: "ΑΓΡ.", LEMMA: "Αγροτικός", NORM: "Αγροτικός"},
    {ORTH: "Αγ. Γρ.", LEMMA: "Αγία Γραφή", NORM: "Αγία Γραφή"},
    {ORTH: "Αθ.", LEMMA: "Αθανάσιος", NORM: "Αθανάσιος"},
    {ORTH: "Αλεξ.", LEMMA: "Αλέξανδρος", NORM: "Αλέξανδρος"},
    {ORTH: "Απρ.", LEMMA: "Απρίλιος", NORM: "Απρίλιος"},
    {ORTH: "Αύγ.", LEMMA: "Αύγουστος", NORM: "Αύγουστος"},
    {ORTH: "Δεκ.", LEMMA: "Δεκέμβριος", NORM: "Δεκέμβριος"},
    {ORTH: "Δημ.", LEMMA: "Δήμος", NORM: "Δήμος"},
    {ORTH: "Ιαν.", LEMMA: "Ιανουάριος", NORM: "Ιανουάριος"},
    {ORTH: "Ιούλ.", LEMMA: "Ιούλιος", NORM: "Ιούλιος"},
    {ORTH: "Ιούν.", LEMMA: "Ιούνιος", NORM: "Ιούνιος"},
    {ORTH: "Ιωαν.", LEMMA: "Ιωάννης", NORM: "Ιωάννης"},
    {ORTH: "Μ. Ασία", LEMMA: "Μικρά Ασία", NORM: "Μικρά Ασία"},
    {ORTH: "Μάρτ.", LEMMA: "Μάρτιος", NORM: "Μάρτιος"},
    {ORTH: "Μάρτ'", LEMMA: "Μάρτιος", NORM: "Μάρτιος"},
    {ORTH: "Νοέμβρ.", LEMMA: "Νοέμβριος", NORM: "Νοέμβριος"},
    {ORTH: "Οκτ.", LEMMA: "Οκτώβριος", NORM: "Οκτώβριος"},
    {ORTH: "Σεπτ.", LEMMA: "Σεπτέμβριος", NORM: "Σεπτέμβριος"},
    {ORTH: "Φεβρ.", LEMMA: "Φεβρουάριος", NORM: "Φεβρουάριος"},
]:
    _exc[exc_data[ORTH]] = [exc_data]

for orth in [
    "$ΗΠΑ",
    "Α'",
    "Α.Ε.",
    "Α.Ε.Β.Ε.",
    "Α.Ε.Ι.",
    "Α.Ε.Π.",
    "Α.Μ.Α.",
    "Α.Π.Θ.",
    "Α.Τ.",
    "Α.Χ.",
    "ΑΝ.",
    "Αγ.",
    "Αλ.",
    "Αν.",
    "Αντ.",
    "Απ.",
    "Β'",
    "Β)",
    "Β.Ζ.",
    "Β.Ι.Ο.",
    "Β.Κ.",
    "Β.Μ.Α.",
    "Βασ.",
    "Γ'",
    "Γ)",
    "Γ.Γ.",
    "Γ.Δ.",
    "Γκ.",
    "Δ.Ε.Η.",
    "Δ.Ε.Σ.Ε.",
    "Δ.Ν.",
    "Δ.Ο.Υ.",
    "Δ.Σ.",
    "Δ.Υ.",
    "ΔΙ.ΚΑ.Τ.Σ.Α.",
    "Δηλ.",
    "Διον.",
    "Ε.Α.",
    "Ε.Α.Κ.",
    "Ε.Α.Π.",
    "Ε.Ε.",
    "Ε.Κ.",
    "Ε.ΚΕ.ΠΙΣ.",
    "Ε.Λ.Α.",
    "Ε.Λ.Ι.Α.",
    "Ε.Π.Σ.",
    "Ε.Π.Τ.Α.",
    "Ε.Σ.Ε.Ε.Κ.",
    "Ε.Υ.Κ.",
    "ΕΕ.",
    "ΕΚ.",
    "ΕΛ.",
    "ΕΛ.ΑΣ.",
    "Εθν.",
    "Ελ.",
    "Εμ.",
    "Επ.",
    "Ευ.",
    "Η'",
    "Η.Π.Α.",
    "ΘΕ.",
    "Θεμ.",
    "Θεοδ.",
    "Θρ.",
    "Ι.Ε.Κ.",
    "Ι.Κ.Α.",
    "Ι.Κ.Υ.",
    "Ι.Σ.Θ.",
    "Ι.Χ.",
    "ΙΖ'",
    "ΙΧ.",
    "Κ.Α.Α.",
    "Κ.Α.Ε.",
    "Κ.Β.Σ.",
    "Κ.Δ.",
    "Κ.Ε.",
    "Κ.Ε.Κ.",
    "Κ.Ι.",
    "Κ.Κ.",
    "Κ.Ι.Θ.",
    "Κ.Ι.Θ.",
    "Κ.ΚΕΚ.",
    "Κ.Ο.",
    "Κ.Π.Ρ.",
    "ΚΑΤ.",
    "ΚΚ.",
    "Καν.",
    "Καρ.",
    "Κατ.",
    "Κυρ.",
    "Κων.",
    "Λ.Α.",
    "Λ.χ.",
    "Λ.Χ.",
    "Λεωφ.",
    "Λι.",
    "Μ.Δ.Ε.",
    "Μ.Ε.Ο.",
    "Μ.Ζ.",
    "Μ.Μ.Ε.",
    "Μ.Ο.",
    "Μεγ.",
    "Μιλτ.",
    "Μιχ.",
    "Ν.Δ.",
    "Ν.Ε.Α.",
    "Ν.Κ.",
    "Ν.Ο.",
    "Ν.Ο.Θ.",
    "Ν.Π.Δ.Δ.",
    "Ν.Υ.",
    "ΝΔ.",
    "Νικ.",
    "Ντ'",
    "Ντ.",
    "Ο'",
    "Ο.Α.",
    "Ο.Α.Ε.Δ.",
    "Ο.Δ.",
    "Ο.Ε.Ε.",
    "Ο.Ε.Ε.Κ.",
    "Ο.Η.Ε.",
    "Ο.Κ.",
    "Π.Δ.",
    "Π.Ε.Κ.Δ.Υ.",
    "Π.Ε.Π.",
    "Π.Μ.Σ.",
    "ΠΟΛ.",
    "Π.Χ.",
    "Παρ.",
    "Πλ.",
    "Πρ.",
    "Σ.Δ.Ο.Ε.",
    "Σ.Ε.",
    "Σ.Ε.Κ.",
    "Σ.Π.Δ.Ω.Β.",
    "Σ.Τ.",
    "Σαβ.",
    "Στ.",
    "ΣτΕ.",
    "Στρ.",
    "Τ.Α.",
    "Τ.Ε.Ε.",
    "Τ.Ε.Ι.",
    "ΤΡ.",
    "Τζ.",
    "Τηλ.",
    "Υ.Γ.",
    "ΥΓ.",
    "ΥΠ.Ε.Π.Θ.",
    "Φ.Α.Β.Ε.",
    "Φ.Κ.",
    "Φ.Σ.",
    "Φ.Χ.",
    "Φ.Π.Α.",
    "Φιλ.",
    "Χ.Α.Α.",
    "ΧΡ.",
    "Χ.Χ.",
    "Χαρ.",
    "Χιλ.",
    "Χρ.",
    "άγ.",
    "άρθρ.",
    "αι.",
    "αν.",
    "απ.",
    "αρ.",
    "αριθ.",
    "αριθμ.",
    "β'",
    "βλ.",
    "γ.γ.",
    "γεν.",
    "γραμμ.",
    "δ.δ.",
    "δ.σ.",
    "δηλ.",
    "δισ.",
    "δολ.",
    "δρχ.",
    "εκ.",
    "εκατ.",
    "ελ.",
    "θιν'",
    "κ.",
    "κ.ά.",
    "κ.α.",
    "κ.κ.",
    "κ.λπ.",
    "κ.ο.κ.",
    "κ.τ.λ.",
    "κλπ.",
    "κτλ.",
    "κυβ.",
    "λ.χ.",
    "μ.",
    "μ.Χ.",
    "μ.μ.",
    "μιλ.",
    "ντ'",
    "π.Χ.",
    "π.β.",
    "π.δ.",
    "π.μ.",
    "π.χ.",
    "σ.",
    "σ.α.λ.",
    "σ.σ.",
    "σελ.",
    "στρ.",
    "τ'ς",
    "τ.μ.",
    "τετ.",
    "τετρ.",
    "τηλ.",
    "τρισ.",
    "τόν.",
    "υπ.",
    "χ.μ.",
    "χγρ.",
    "χιλ.",
    "χλμ.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = _exc
