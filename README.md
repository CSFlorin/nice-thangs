In my student cooperative at uni, I gave a platform for members to leave comments for each other at the end of the semester. With 42 people, it would have taken quite a while to compile these into a nice printed note for each person, so I made a quicker way to do it.

1. Make a Google Form following [this template](https://docs.google.com/forms/d/e/1FAIpQLScE2oANQzqG4JZ_Jf6JZ01Zc6eP3knVI77MffDL0sqkJyRVLQ/viewform?usp=sf_link).

2. Download the responses as a CSV.

3. `python3 -m virtualenv env`

4. `source env/bin/activate`

5. `pip install -r requirements.txt`

6. `python nice-thangs.py`

7. Select all the files in `out/` and press `Command+P` to print them.
