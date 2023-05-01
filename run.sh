if [ ! -d venv ]; then
  python3 -m pip install virtualenv
  python3 -m virtualenv venv
fi

if [ ! $WORKER_COUNT ]; then
  export WORKER_COUNT=4
fi

if [ ! $SERVER_PORT ]; then
  export SERVER_PORT=5000
fi

source venv/bin/activate

python3 -m pip install flask uwsgi requests

uwsgi --master -p $WORKER_COUNT --http 0.0.0.0:$SERVER_PORT -w app:app



