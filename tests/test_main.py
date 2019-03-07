import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_extraer_emails():
    s = "Escribe a a@b.com y c.d+z@dom.es."
    assert sorted(mod.extraer_emails(s)) == ["a@b.com","c.d+z@dom.es"]
    assert mod.extraer_emails(None) == []
