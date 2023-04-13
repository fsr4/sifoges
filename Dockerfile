FROM python:3.11
WORKDIR /app

# Install XeTeX
RUN cd /tmp && \
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    zcat < install-tl-unx.tar.gz | tar xf - && \
    rm install-tl-unx.tar.gz && \
    cd install-tl-* && \
    perl ./install-tl --no-interaction --scheme=small --no-doc-install --no-src-install && \
    cd .. && rm -r install-tl-*

RUN ln -s /usr/local/texlive/*/bin/* /usr/local/texlive/bin
ENV PATH="/usr/local/texlive/bin:$PATH"

# Install fonts
COPY resources/font/*.ttf /usr/local/share/fonts/
RUN fc-cache

# Install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY resources/* ./resources/
COPY generate-* ./

ENV SIFOGES_DIR="./data"
VOLUME "./data"

ENTRYPOINT ["./generate-slides.sh"]
