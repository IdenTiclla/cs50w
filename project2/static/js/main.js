// force user to input data
function callPrompt(msg) {
  tag = prompt(msg);
  if (tag == null) {
    callPrompt(msg);
  }
  return tag;
}


// When the document content is loaded
document.addEventListener("DOMContentLoaded", () => {
  // settings of colors
  document.querySelector("#app_name").style.color = "green";
  document.querySelector("#welcome").style.color ="#" + Math.random().toString(16).substr(-6);
  // if can't get username
  if(!localStorage.getItem("username")) {
    var username = callPrompt("enter value");
    localStorage.setItem("username", username);
    document.querySelector("#chat").style.visibility = "hidden";
  }
  document.querySelector("#welcome").innerHTML = `Welcome: ${localStorage.getItem("username")}.`;

  // Connect web socket
  var socket = io.connect(
    location.protocol + "//" + document.domain + ":" + location.port
  );
  // when socket is connected
  socket.on("connect", () => {
    // if the user was in a room before they left send them back to that room
    if (localStorage.getItem("channel") && localStorage.getItem("username")) {
      document.querySelector("#chat").style.visibility = "visible";
      const channel = localStorage.getItem("channel");
      const username = localStorage.getItem("username");
      socket.emit('if channels');
      socket.emit("join_channel", data={"channel":channel, "username":username});
    } else if(!localStorage.getItem("username")) {
      var username = callPrompt("enter value");
      localStorage.setItem("username", username);
      document.querySelector("#chat").style.visibility = "hidden";
    }
  });
  // Every 1 sec ask to the server if there are channels.
  setInterval(() => {
    socket.emit('if channels');
  }, 1000);

  // Receibe this event when there are channels
  socket.on("if channels",data=>{
    document.querySelector("#chat").style.visibility = "visible";
    const channels = data["channels"];
    document.querySelector('#channel_list').innerHTML = "";
    for(let j = 0; j < channels.length; j++){
      const button = document.createElement('button');
      button.innerHTML = `${channels[j]}`
      button.dataset.channel = `${channels[j]}`;
      button.onclick = ()=>{
        const channel = button.dataset.channel;
        const username = localStorage.getItem("username");
        localStorage.setItem("channel", channel);
        socket.emit("join_channel", {"channel":channels[j], "username":username});
      };
      document.querySelector("#channel_list").append(button);
    }
  });

  // Execute when the user clicks on button logout
  document.querySelector("#logout").onclick = () => {
    socket.disconnect();
    localStorage.clear();
  };
  // Execute when the user create a new channel
  document.querySelector("#create-channel").onsubmit = () => {
    const channel = document.querySelector("#channel_name").value;
    const button = document.createElement('button');
    button.innerHTML = `${channel}`;
    button.dataset.channel = `${channel}`;
    
    button.onclick = ()=>{
      const channel = button.dataset.channel;
      const username = localStorage.getItem("username");
      localStorage.setItem("channel", channel);
      socket.emit("join_channel", {"channel":channel, "username":username});
    }
    
    document.querySelector("#channel_list").append(button);
    document.querySelector("#channel_name").value = "";
    socket.emit("channel_creation", channel);
    // prevent form submision
    return false;
  };
  // It executes when a channel-name already exists
  socket.on("channel_error",(data)=>{
    alert(`${data["error"]}`);
  });
  // It executes when the user join in a channel
  socket.on("join_channel",(data)=>{
    // Use the channel as the chat's header
    document.querySelector("#chat_header").innerHTML = data["channel"];
    // Save the channel in the client's memory for later use
    localStorage.setItem("channel", data["channel"]);
  });
  
  // Execute when the user receives a message
  socket.on("receiving messages", data => {
    // in memory
    const channel_memory = localStorage.getItem("channel");
    const channel = data["channel"];

    if(channel_memory == channel){
      // Clear the messages area
      document.querySelector("#lista-chat").innerHTML = "";
      // Fill up the messages area with the channel's name
      const messages = data["messages"];
      var x;
      for (x in messages) {
        const user = messages[x].user;
        const message = messages[x].msg;
        const time = messages[x].time;
        const channel = localStorage.getItem("channel");
        var json = {user:user, message:message, time:time, channel:channel}
        // create a new element li
        const li = document.createElement("li");
        const div = document.createElement('div');
        div.classList.add("chat-body", "white", "p-3", "ml-2", "z-depth-1", "header");
        const divhijo = document.createElement('div');
        const strong = document.createElement('strong');
        strong.classList.add("primary-font");
        strong.innerHTML = messages[x].user;
        const small = document.createElement('small');
        small.classList.add("pull-right", "text-muted");
        small.innerHTML = ` ${messages[x].time}`;
        const button = document.createElement('button');
        button.type = "button";
        button.classList.add("close");
        if(localStorage.getItem("username") == user){
          const span = document.createElement('span');
          span.setAttribute("aria-hidden","true");
          span.innerHTML = "&times;"
          div.innerHTML = `<span ">&times;</span>`
          button.appendChild(span);
        }
        
        button.onclick = ()=>{
          socket.emit('delete message',{
            msg: message,
            user: user,
            channel: channel,
            time: time
          });
        };
        const hr = document.createElement('hr');
        hr.classList.add("w-100");
        const p = document.createElement("p");
        p.classList.add("mb-0");
        p.innerHTML = messages[x].msg;
        
        divhijo.appendChild(strong);
        divhijo.appendChild(small);
        divhijo.appendChild(button);
        
        div.appendChild(divhijo);
        div.appendChild(hr);
        div.appendChild(p);

        li.appendChild(div);
        
        // add the element to the list of message
        document.querySelector("#lista-chat").append(li); 
      }
    }
  });

  
  // Execute when the user click on button send message
  document.querySelector("#button_send").onclick = () => {
    // Send a JSON to the server with the channel, the message and the user's name in it
    const msg = document.querySelector("#text-field").value;
    const user = localStorage.getItem("username");
    const today = new Date();
    const time =
      today.getHours().toString() + ":" + today.getMinutes().toString();
    const channel = localStorage.getItem("channel");
    document.querySelector("#text-field").value = "";
    
    socket.emit("sending message", {
      msg: msg,
      user: user,
      channel: channel,
      time: time
    });
    
  };
});
