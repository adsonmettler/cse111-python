assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Adson", "N") == "N; Adson"
    assert make_full_name("Sally", "") == "; Sally"