# -*- coding: utf-8 -*-
import re
import re

def extraer_emails(s):
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", s or "")

