from flask import Flask, request, redirect, render_template, session, jsonify, make_response, json
import CXServices.cxservice_index as cxindex

app = Flask(__name__)


@app.route('/cxtksearch/api',methods=['GET','POST'])
def cxtksearch():
    if request.method == 'GET':
        print(request.form)
        services = '2'
        Title = '软件工程'
        Anser = '2'
        li = []
        res = cxindex.GetIn(services, Title, Anser)
        print(res)
        for item in res:
            print(item)
            li.append(item)
        return render_template('BRsearch.html', content=li)
    else:
       # print(request.form)
        services = request.form.get('ServiceType')
        Title = request.form.get('Title').replace("/","").strip().replace('\n', '').replace('\r', '')
        Anser = request.form.get('Anser')#.replace("/","").strip().replace('\n', '').replace('\r', '')
        #print(services,Title,Anser)
        #print(str(cxindex.GetIn(services,Title,Anser)))
        #response = make_response(json.dumps(cxindex.GetIn(services,Title,Anser),ensure_ascii=False))
        # response.mimetype = 'apllication/json'
        li = []
        res = cxindex.GetIn(services, Title, Anser)
        print(res)
        for item in res:
            print(item)
            li.append(item)
        return render_template('BRsearch.html', content = li)



if __name__ == '__main__':
    app.run()
