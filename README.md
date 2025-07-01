# murgenere-web

This repository contains a small Flask application used to serve
`murgenere.com` and `my.murgenere.com`.

## Installation

Run the provided `setup.py` script to create a virtual environment,
install dependencies and clone the private Streamlit repository:

```bash
python setup.py
source .venv/bin/activate
```

## Running

```
python -m app.main
```

If `/my` should be protected, set `MY_USERNAME` and `MY_PASSWORD` in the
environment before launching the server.

The root page (`/`) will display an image for `murgenere.com`.

Accessing `/my` will redirect to a Streamlit application assumed to be
running locally. Set the `STREAMLIT_URL` environment variable if the
Streamlit app runs on a different URL.

The setup script clones the
[`filippobounous/personal`](https://github.com/filippobounous/personal)
repository under `./personal`. Launch its Streamlit interface with:

```bash
cd personal
streamlit run app.py
```

Once running, visiting `/my` on this Flask server will redirect to the
Streamlit app (default `http://localhost:8501`).
Authentication for `/my` is optional; provide `MY_USERNAME` and
`MY_PASSWORD` environment variables to enable HTTP basic auth.
