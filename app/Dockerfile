FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-xetex \
        texlive-lang-portuguese \
        texlive-publishers \
        texlive-science \
        texlive-humanities \
        texlive-bibtex-extra \
        texlive-fonts-extra \
        texlive-plain-generic \
        abntex \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
