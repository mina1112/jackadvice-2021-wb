from controllers import *


# FastAPIのルーティング用関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin, methods=['GET', 'POST'])
app.add_api_route('/todo/{t_id}', detail)
app.add_api_route('/add', add, methods=['POST'])
app.add_api_route('/delete/{t_id}', delete)

"""
app.add_api_route('/get', get) 
app.add_api_route('/add_task', insert, methods=['POST'])
"""