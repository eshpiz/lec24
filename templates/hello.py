

{% if firstname == '' %}
<h2> What is your name? </h2>
{% else %}
<h2> Hello {{firstname}} {{lastname}} </h2>
Would you like to change your name? <br/>
{% endif %}

<form action="/hello" method="POST">

    First Name: <input type="text" name="firstname"/> <br/>
    Last Name: <input type="text" name="lastname"/> <br/>

    <input type="submit" value="submit"/>

</form>
