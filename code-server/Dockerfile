FROM linuxserver/code-server:latest

USER root


WORKDIR /config/workspace/backend/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        openjdk-17-jre \
        graphviz \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -L -o /usr/local/bin/plantuml.jar \
    https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar


# --- Install Astral's uv system-wide ---
# This installs uv into /usr/local/bin so all users (incl. abc) can use it.
RUN curl -fsSL https://astral.sh/uv/install.sh | \
    UV_INSTALL_DIR=/usr/local/bin sh

# Make sure config/workspace exists before copying your settings
#RUN mkdir -p /config/workspace

COPY ./pyproject.toml ./uv.lock /config/workspace/backend/

COPY install-extensions.sh /usr/local/bin/install-extensions.sh
COPY ./extensions/ /config/workspace/.vscode/
RUN chmod +x /usr/local/bin/install-extensions.sh


# RUN mkdir -p /config/.mpe-extensions
# COPY .markdown-preview-enhanced.json /config/.mpe-extensions/.markdown-preview-enhanced.json

# RUN chown -R abc:abc /config/.mpe-extensions

# RUN mkdir -p /config/extensions && chown -R abc:abc /config


#plantuml
RUN mkdir -p /config/data/User/
RUN echo '{\
    "markdown-preview-enhanced.usePlantumlJar": true,\
    "markdown-preview-enhanced.plantumlJarPath": "/usr/local/bin/plantuml.jar",\
    "git.autofetch": true,\
    "chat.disableAIFeatures": true,\
    "github.copilot.enable": {"*": false}},\
    "github.copilot.inlineSuggest.enable": {"*": false}\
}' > /config/data/User/settings.json
RUN chown -R abc:abc /config/data

RUN uv venv /config/workspace/backend/.venv
WORKDIR /config/workspace/backend
RUN uv sync --python /config/workspace/backend/.venv/bin/python
# Add user-local bins to PATH (kept from your original)
ENV PATH="/root/.local/bin:/config/.local/bin:${PATH}"
ENV PATH="/config/workspace/backend/.venv/bin:${PATH}"



RUN /usr/local/bin/install-extensions.sh


# RUN uv venv ./config/workspace/backend/.venv --clear
# RUN . ./config/workspace/backend/.venv/bin/activate
#RUN uv sync --active
