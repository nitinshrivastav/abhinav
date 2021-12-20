#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def web(): 
    return render_template('abc.html')
@app.route('/data',methods=['GET','POST'])
def extract():
    if(request.method=='POST'):
        num1=request.form['a']
        num2=request.form['b']
        total=int(num1)+int(num2)
        print(num1)
        print(num2)
        print("Total : ",total)
        return render_template('abc.html',my=total)
if __name__=='__main__':
    app.run()

