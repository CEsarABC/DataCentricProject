{% extends 'base.html' %} 

{% block content %}
<div class='row'>
        <ul class="collapsible" data-collapsible="accordion">
                
            {% for task in tasks %}
            
            <li>
                <div class="collapsible-header">
                  <div class="col s3">
                          <i class="material-icons">expand_more</i>
                          <a href="{{url_for('delete_task', task_id=task._id)}}" class="waves-effect waves-light btn btn_small">Done</a>
                          <a href="{{url_for('edit_task', task_id=task._id)}}" class="waves-effect waves-light btn btn_small blue">Edit</a>
                  </div>
        
                  <div class="task_header col s9">
                        <strong>{{task.task_name}}</strong>  - {{task.due_date}}
                        {% if task.is_urgent == 'on' %}
                          <strong>this is urgent</strong>
                        {% endif %}
                  </div>
                  <div>
                      
                  </div>
                </div>
                <div class="collapsible-body">
                    <span>
                        {{task.task_description}} 
                    </span>
                </div>
            </li>
            
            {% endfor %}
        
        </ul>
</div>

{% endblock %}