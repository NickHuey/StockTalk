import bitdotio
import psycopg2
from pprint import pprint

b = bitdotio.bitdotio("6tRy_stJmCxtHWUs6uxp64yJQByA")
pprint(b.list_repos("CasualCoder"))

conn = b.get_connection()
cur = conn.cursor()
cur.execute('SELECT "Symbol", "Name", "Last Sale", "Sector", "Volume" FROM "CasualCoder/stock_ticker"."nyse" where "Volume" >=2000000 order by "Volume" desc')
# cur.execute("SELECT 1")
pprint(cur.fetchall())
