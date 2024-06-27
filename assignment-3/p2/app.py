from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, select
import time, datetime


app = Flask(__name__)

# Update the below configuration with your existing PostgreSQL database details
psql_user = 'postgres'
psql_password = 'slouch-fest-concept-farrier'
db_name = 'pits'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@localhost/{}'.format(psql_user, psql_password, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    # Execute a raw SQL query directly
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Stock WHERE sym = 'AAPL';")
    query_result = cursor.fetchall()
    if len(query_result) > 0:
        res = query_result[0]
    else:
        res = []
    return jsonify(res)


@app.route('/getOwner')
def getOwner():
    """
        This HTTP method takes aid as input, and returns the owner's pid
    	If the account does not exist, return {'pid': -1}
    """
    aid = int(request.args.get('aid', -1))
    query = text("Select pid from Owns O where O.aid = :aid;")
    pids = db.session.execute(query, {"aid": aid}).scalars()
    response = [{"pid": int(pid)} for pid in pids]
    return jsonify(response or [{"pid": -1}])

@app.route('/getHoldings')
def getHoldings():
    """
        This HTTP method takes aid and sym as input,
        and returns the total share of holdings for a stock sym of an account
        If the stock or the account does not exist, return `{'shares': -1}`;
        if the account does not hold any share of the stock, return `{'shares': 0}`.
        Otherwise returns `{'shares': total_share}`.
        Do NOT use the view you defined in P1.
        """
    aid = int(request.args.get('aid', -1))
    sym = request.args.get('sym', '')
    validation_query = text("select exists(select aid from account where aid=:aid) and exists(select sym from stock where sym=:sym);")
    aid_and_sym_exists = db.session.execute(validation_query, {"aid": aid, "sym": sym}).scalar()
    shares = -1
    if aid_and_sym_exists:
        query = text("select coalesce(sum(case when type = 'buy' then shares else shares * -1 end), 0) as shares from trade T where T.sym = :sym and T.aid = :aid")
        shares = db.session.execute(query, {"sym": sym, "aid": aid}).scalar()
    return jsonify({'shares': shares})

def currentTime():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
@app.route('/trade')
def trade():
    """
        This HTTP method takes the information of a trade as input: aid, sym, type, shares, price 
        You need to retrieve the current maximum seq numer (max_seq) for aid and 
        then insert with max_seq+1 and the current timestamp.
        It returns {'res' : 'fail'} if there is an oversell;
        Otherwise, it returns {'res': the current seq} and also updates the database accordingly.
        You should implement the check of the violation in the Python function 
        and DO NOT use the view you implemented in P1.
        You will need to finish a multi statement transaction in this function.
        
        Ideally, you need to send a HTTP POST request for such editing requests, 
        but we just choose GET for easier test
    """
    aid = int(request.args.get('aid', -1))
    sym = request.args.get('sym', '')
    type = request.args.get('type', '')
    shares = float(request.args.get('shares', -1))
    price = float(request.args.get('price', -1))
    validation_query = text("select exists(select aid from account where aid=:aid) and exists(select sym from stock where sym=:sym);")
    shares_query = text("select coalesce(sum(case when type = 'buy' then shares else shares * -1 end), -1) from trade T where T.aid=:aid and T.sym=:sym")
    aid_and_sym_exists = db.session.execute(validation_query, {"aid": aid, "sym": sym}).scalar()
    total_shares = db.session.execute(shares_query, {"aid": aid, "sym": sym}).scalar()
    is_not_oversell = type == 'buy' or total_shares >= shares
    res = "fail"
    if aid_and_sym_exists and is_not_oversell:
        latest_seq_id = db.session.execute(text("select coalesce(max(seq), 0) from trade where aid=:aid"),
                                           {"aid": aid}).scalar() + 1
        latest_trade_query = text("select coalesce(max(timestamp), current_timestamp) from trade where aid=:aid")

        latest_trade_time = db.session.execute(latest_trade_query, {"aid": aid}).scalar()

        add_trade_query = text("Insert into trade values (:aid, :seq, :type, :timestamp, :sym, :shares, :price)")
        db.session.execute(add_trade_query, {"aid": aid,
                                             "seq": latest_seq_id,
                                             "type": type,
                                             "timestamp": latest_trade_time,
                                             "sym": sym,
                                             "shares": shares,
                                             "price": price})

        res = latest_seq_id

    return jsonify({"res": res})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
