import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJztXOtv29YVv5TfatImTZqkddPevjKnaRxbSuIm6YuWFVuxRHmU1CRyE4M2GYmxSKkk1SRtgq1IBgTYsMatHaPZAnQoUCDY1g4bMGAY+m1/iT/s6z5tX7t7Dnmpt2oXzpwOkqnLw/s4997zO4c891qHC8T7dLHvO+xrv8ASlR0CKRCSJUQj5LJA1AC5KUBmd4YlqSGorn/HPpL9wRlCFjibHs6mHKhl49ECyQqcDpBsgNNdJNvF6W6S7eZ0D8n2cLqXZHs53UeyfZzuJ9l+Tg+Q7ACngyQbRDpACo8RYxvJbiPCtR28eDvJbidnzedIt/Y4WQwS6x9EEASY7hNE7YLpCmaInKs02EGyO2oa/LuqQbfbQCDn1B5yi015J1F7kXiSqH1I7CJqPxK7iTqAxFNEDSKxh6iPIbGXqNuQ2Ec8xtuRsfo4yT5NtKfJ5JT2DFGfgMzsYF0dNtKdZPfklPokq6buItog2csInq3tIzcJq7YbSp+CZA8keyHZBwlwV5+BLp4l6iB2sZ9o+4n6LFkMEGtN0PYgB20nnsxPsHA/FnYHeOEut5fnGB/TwBrPY42f+DXcQVNXYmewygtYJRLwyl50y4ax7CUsez9QO9mXYZxuzitubUQpNXTAV80hgZFOkCXpvKUp6kyxWLD3sMuSXgpR3bQdpVCghraQV0z9Q81+qr7I0t4va7Zj++rNlJpEQL13AmfXMgR3PIR1DcWS/QpUyNN5ZV6fmy8rztw1xczNmTnN0haKqjbnsO4W7WE7j/UdSIq20wutrtmOZgxBT5XEhgpqDuehmY5mOTCNXbyECDg6mGo3H91L/uhuYAeXu8h1AgdkdpNfBbzxQiNpCGzW6fK6x16uagtlR5kvaDJKsMfLKzjQg2LlPnAl28cSM1cusOk1DhcKLSY8xXJA5HY3jnJA2Jgskyy9quYOF0uaSfOOU7JPHjmilPThK3nFsZVSaXihaByxNVN9u5Qvmtqbx0OvHzt+NBQaPRYKv37A0a46b4q2rRQUo8wSfbFsIGecmByoEXTN8OF0RXmmTso1436xYdwBppOsJep/FxgTTAQmLqEMFwqaYtnfMgZ0bfmTteWP11a+Xlv5IxDLn9Gqz+Ds6KnwmDGL57BxyLu+QNPJZDxFp8TINBXjcRqTaFKKBt36o8ba8k3ku7q2/BvGkV3WMDxmvMo5i2UnX7R4u5MucdxIlPOKoah0SjFUxaSp4rxu6WaF/8qfgO3dX8LBOlr5pmHIUUPRC7SOccgAhkzrS8q1d3JQA1AL+lxdCfwdpfFnHP7HlcMV0crXVZ2cL5ad8rzWrBM26uSlS/qCrhSCVVK5+2s4GMH41x3LX2Iv39QLKWykwc7ouGbptk5DI9S9nlIWFnUzNxysFgob6V9gBnd/wTjVsr9ZJZ+wcUYp53UaVyxmM2ys59mJiqriT+3i3EVf3LSK9WcILCdcwXvjPcR5TzHLVHTqYTutWJqp0IRmKIuKHvQbgEBWYaygIx5RNUBGpXVVWaQpzS4XdAcYwE2MD/Dk4Qn788NMg11mayvLayt3Go7VFvmbcrRivhr0JLK2ssSHS6Ukp2iltKrCR57yTIin06JcbWDxqDQ5Lc549W7UNh+cHTFSaTGdSVWyK93faza8+y3yN+Voxfx+RU0fOaBGjSY4jIzWCnyU41Vzm6mgJk/T02IkOp5MTvsNq6qOtoA7KTXppjKsDoA/HMBQCwDr6iUy8XSMjsuZdPR0Uo5EG2HsALg1AIbXhwDeJGMSuwtOymLCN80hz5eQklROJtNe7sF1w1l5+HXg3BQ4j24AzoQYi1O0zIphduxxiwE81u6JWFf53Zicjp6jZ6fEdEqcqTgvnSfiFgJ4vDWAzb3Qs9HxVCwdpe9m4lI1hB0AtwbAsbY+aQOKqRl4HqYSqTqPdN0Adp6Bmwzg6+0BrKseYXdPSsWJREyqR7AD4NYAeKINgHV1zyRjElvBJyZEiaaS4zG5DsUOhFsC4ejIBtwYdEbPxk7H6lcVVUuKjlOzpXC23qdpv05sDejBKmA7qG4Nqq02b5o/KBFaOpOJp8S2D8qaZqNGJBmbqLvNdgDcJABbbd40hW4iJiaS0gSlp+VolJ6OyZXFfhsAw0ZCjNU/JzsAbhKArbZr2hhgJsJscHyyzgQ7AG4NgG23a5oDGJmhkeREogPgIwFgm+2aJgiOZybpVEZKR+WG5X7HidkaAL9vu6YBw+nDE0m5/v+HHQC3DMCNbdekouDCvBuTMx0LfEQAbLdd0wDfVFJOS1GZ0nhMmq6DsAPglgAYar1ZU1dTypzPxKk4E49Ni6kYjYgzManaE+0AuDUAttyeaY8fPR0XU1OTyQqCHQC3BsB2OzHNFhF8LZ+Ij4/X3ENbLyM6OzFbA2Az+PivnyhNi/JktHqT+//FAn9sCI6s/z8WR43paDwjMh9mRk7CNvf3ejGjRvRcLP3IY/Yjg+zQoQ1AlsqMR+TYeJTOiGfE5E/X4XiyFqlHHTIMzaqEN2AcRqGo6mYu1CLUYYCdDM0sY1zJfijox4iH7UKP0OfGPXRVxz1caxr3gAEPTsCLhLrBOGPgVqGL3BAgBkXtxfwAuR6AgCgI6ZmHkBS136PVAWDQTS73EMHcBZFR7LIXgynYJDCmAsIpHoNwChlS+yKbJUIQdhX0q4cm7QYV9PQiVVaVPC2VzWsKjU1QCD+YUWz7StFSKct7G/97jEh9+TBNpUYBgtjTpijfql0iVSJeiicnYxLNSOnMNE1E46J0JpOeFiV3kl9s1gTs7axTxpMJFD8nKYZz8eyZszwbddsLUkHaCzOxQ25Nd7ipzHQqmgq2kgfM7gSz4bt/xbCpeDGnm3RSnBTjr9GUXlDyiwzUfHm+bOZ09zchQ/21Fgb2YylX5nSzVHZwHDnNKTE1kCH0B2OmtKu6I0NoldPvhkXZTtnS0FSxvGxrlryTx1rZiqnqDXYqQ8jXy3C9zzfPHmEb/u1jVDDgmys06OPmKhMMjGNGykyUWSekAcjJ9YGZXh0BK5y4MAR2ymz2ukD2TrrmfdkNZXK6IGjMtV/h/RfJWbTDPozPghkwLPA8zM/D/DxsH2Tn7Z6IEbXZtdVPLuA99ETIiBcVuDG5l2NG7hJ+/vk2hqS50sOwOEctMslC5qVC2c6jyBzd0FxpFTSt5IbSYSSb7uiLDqBTbLzVocD1RdAPO4iSGmRy7GdfX24fcrn9XqiTW4d+qHQPyX3YqJC9rRWyz1XIjwRXIft9hZy9fsE9H/HOh73zexcw2HDW8xbWfvsZxPFcCGIoH1fTGg2N5LWFRV8/730On79V6acMsY3yXkjAKuWnQeMC3NALRffBKw82e/DK29jpFFxvQ+X7jpTrlfEAV8Zvaow4sEG6VYX2zbtJ7sAPuUP8rPoOgQbs/hrL7nVvFuzj3rndH2fZfX6NoP2mD8QYPNM5Uoe8LB+XFPPEXOctMiVKUjTuFhzfGEaeb5TXLacFRJQD4N4trnoAuf7Hgx734ciUZq7qE/QGTeHpv3b303YHdyIfTu3B2fDoqVGsvMwdatcLWeUOk+9lg1sdDp/CX7yt01NZZdYDv+GhrjeEh+sFfNmYU8V+nY7JfdZizG3hejMsfcAuHtSegnwUlO9vHGdP89ttjmq3vWoOX/GJN4roKyjm7n5jR42rpNVKeV1hs5Ilz8WiKK0H2GWjIJe83yKGQ6cqjSpDwGlgtkf9waeWUZiVbr1smH7dZBrY0KYy5xjeby386l7uNO+/Wb/3WlR9j8Ktmjnc8/aCpc9r1R3fq5Fqa9Q9XjAa5BZhvqKpFSqsPF5cbR/UHvdxWTjSJM6YN/cNwR8Rc5uXb3uaj2NAjV67e6eFSt79FHoY/te3vysmK/rWRuO+QBV1j9XaFm3FgjNpGgbuB1Lz8O8qpo3Ge59yqYiR6ajcwCtyfpzlpqNigiXMqfaim8PGG/+T1dCdt/jw7df4UoY94l+9wMeXENn6QJSoJCZEOi0mMn4wvE75fd9/Ht2x/4OXaIEUBbnEj9vu9c/ZUSlh1C034xYW3XKLbmHprZpGQb/V7Zb8vOZLtK5Ss0bAbwlJL6VuvsuvQi1VTn4lf1JVVe3D/tO7/h/pVQIdM6Z0LkBfdmGQ3ZI9U335hUfNehxe9a59YGZi8dgUW2VKGem8SFvVtsfcpV7N1k7YqPvvx1HDXdZBBD9blnuFttS0bai+7RRf/HFrGfF+vRoyzsJbKMRSyWtysMVwwvUsY94LRsYVdgviw3mraduj9W0nilfMAls40QxbNNIDuOHAWQw1YTFqNOxjRtlydNh+vhqPezVLYU/jqQ7rKB18ITvMkqBXPa1ZOrxWwNbzNK2xNTJNaGYuVzYVWCy770mImTq9OHdRxxeLPMGSeYW/FKVQHrbzOrhmdoY0eb8HW0wP53QHFt1sigtF09FMB1/0kXcX+KMnTowdKRQXFKdojR4xFNvRrCMgB/fONexcdXT04kKVKW5gzPKT4AY+R/gqv5u7jujUq4qj4eIT3FmLLdWLBjqSeTa/gj6Pbw6xNNwVcPC1M2wFgCvWy3bRdBf50LJsFaD2bkYa5YKjl6zigmbb8GqJEhsMrNqJtzXnvZ/GAaczZpSKlhO1rKIl++sM/p4aGff+oBFuNsiwY4LbBvKzkMAyAz1ab3GSK5qKock7iPeWHHy7DGQt4kra3c8AqqQX9HyL3UNg9YZRVMsF7S1UlEssuSXs6O0SdjBPeWeAnwe6BrrZt2/g8YGBgf6B/u1CL+5fbA8MsPMA++vDHY3KH+xs9AlBTPuY3w3nHSyFL+x+VJx4Q7HsvFLAwYJt2OsYrMDztwn/BblVYPY="))))