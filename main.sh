VENV_DIR="venv"

# create virtual environment if it does not exist
if [ ! -d "$VENV_DIR" ]; then
    python -m venv "$VENV_DIR"

    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment"
        exit 1
    fi
fi

# Check if the virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    source "$VENV_DIR/bin/activate"
    
    if [ $? -ne 0 ]; then
        echo "Failed to activate virtual environment"
        exit 1
    fi
fi

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "Failed to install dependencies"
        exit 1
    fi
fi

python main.py
