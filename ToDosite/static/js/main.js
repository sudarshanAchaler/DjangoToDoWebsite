var updateBtns = document.getElementsByClassName('updateTask')

for(let i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(e){
        e.preventDefault()
         var taskId=this.dataset.id
         var action= this.dataset.action
         console.log('taskId:', taskId, 'Action:', action)

         updateTask(taskId, action)
    })  
}

function updateTask(taskId, action){
    var url='/UpdateTask/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'taskId':taskId, 'action':action}) 
    })
    .then((response) => {
        return response.json();
     })

     .then((data)=>{
         console.log('data: ',data)
         location.reload()
     })

    
}