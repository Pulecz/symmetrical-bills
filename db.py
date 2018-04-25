#!/usr/bin/env python
from sqlalchemy import create_engine  # motor
from sqlalchemy import Column  # structure
from sqlalchemy import Boolean, DateTime, Integer, String, Unicode  # datatypes
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# one table for the actuall bills
"""
Column(From)
Column(DateTime)
Column(Location)
Column(BKP)
Columnt(FIK)
CONTENTS> ammount and linkers to a product with specific price
Additionals specific to From(Company giving the bill)
"""
Boolean()
Column(DateTime)
# contents
Amount = Integer()
Product = Unicode()

# what is String for if we have Unicode?
String()

# second table contents
"""
product, many details, mainly price at the current time
"""
create_engine()
Column('Product')
