"""Trafaret schemas for data validation."""

import trafaret as t


ADDRESS_DATA_SCHEMA = t.Dict({
    t.Key('country'): t.String,
    t.Key('city'): t.String,
    t.Key('state'): t.String,
    t.Key('zip'): t.Int(gt=0)})
