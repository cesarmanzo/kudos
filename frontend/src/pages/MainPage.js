import { useEffect, useState, useReducer } from 'react'
import { useAuthActions, useAuthUser } from 'use-eazy-auth'
import React from 'react';
import Swal from 'sweetalert2'


const formReducer = (state, event) => {
 return {
   ...state,
   [event.name]: event.value
 }
}


function App() {

  const { user } = useAuthUser()
  const { logout } = useAuthActions()
  const [kudosreceived, setKudosReceived] = useState([])
  const [kudossent, setKudosSent] = useState([])
  const [userData, setUserData] = useState([]);
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useReducer(formReducer, {});


  const handleSubmit = event => {
    event.preventDefault();
    kudosPost(formData);
    Swal.fire("Kudos Sent!" ,'Keep it up!', "success").then((result) => {
      if (result.isConfirmed) {
        window.location.reload();
      }
    })
  }

  const handleChange = event => {
    setFormData({
      name: event.target.name,
      value: event.target.value,
    });
  }


  function kudosPost(formData) {
    var json_token = JSON.parse(localStorage.auth)
    fetch("http://localhost:8000/kudos-post/", {
    method: 'POST',
    body: JSON.stringify(formData),
    headers: {
    Authorization: `JWT ${json_token.accessToken}`,
    'Content-Type': 'application/json;charset=UTF-8'
  },})
  }


  useEffect(() => {
    async function getUsers() {
      var json_token = JSON.parse(localStorage.auth)
      const response = await fetch("http://localhost:8000/users-available/", {
        headers: {
        Authorization: `JWT ${json_token.accessToken}`,
        },
      });
      const data = await response.json();
      setUsers(data.results)

    }
    getUsers();
  }, []);


  useEffect(() => {
    async function getUserData() {
      var json_token = JSON.parse(localStorage.auth)
      const response = await fetch("http://localhost:8000/user-data/", {
        headers: {
        Authorization: `JWT ${json_token.accessToken}`,
        },
      });
      const data = await response.json();
      setUserData(data.results[0])

    }
    getUserData();
  }, []);


  function kudosReceived() {
    var json_token = JSON.parse(localStorage.auth)
    fetch("http://localhost:8000/kudos-received/", {
    headers: {
    Authorization: `JWT ${json_token.accessToken}`,
  },})
    .then(res => res.json())
    .then((kudosreceived) => {
        setKudosSent([])
        setKudosReceived(kudosreceived.results)
      })
  }

  function kudosSent() {
    var json_token = JSON.parse(localStorage.auth)
    fetch("http://localhost:8000/kudos-sent/", {
      headers: {
        Authorization: `JWT ${json_token.accessToken}`,
      },
    })
    .then(res => res.json())
    .then((kudossent) => {
        setKudosReceived([])
        setKudosSent(kudossent.results)
      })
  }


  return (
    <div className="row mt-2 p-2">
      <div className="col-md-6 offset-md-3">
        <div className="mb-3 text-center">
          <h1>
            Welcome, <i>{user.first_name} {user.last_name}</i>
          </h1>
          <br/>
          <h4>
            Member of <b>{userData.organization}</b>.
          </h4>
          <br/>

          <b>
            You have {userData.kudos_available} kudos remaining. They expire/renew at the end of the week!
          </b>
          <br/>
        </div>

          <form onSubmit={handleSubmit}>
          <fieldset disabled={userData.kudos_available === 0}>
            <div className="form-group">
              <label form="send_to">To:</label>
              <select className="form-control" id="sent_to" name="sent_to" onChange={handleChange} value={formData.sent_to || ''}>
                <option key="0" value="0">--Who will received the kudos?--</option>
                {users.map(user_list => {
                  return (
                    <option key={user_list.user.id} value={user_list.user.id}>{user_list.user.first_name} {user_list.user.last_name}</option>
                  );
                })}
              </select>
            </div>
            <div className="form-group">
              <label form="message">Message:</label>
              <textarea className="form-control" id="message" name="message" rows="3" onChange={handleChange} value={formData.message || ''}/>
            </div>
            <div className="form-group text-right">
            <button disabled={!formData.sent_to} type="submit" className="btn btn-primary">Send Kudos</button>
            </div>
            </fieldset>
          </form>

        
        <br/>
        <div className="text-center">
          <button onClick={kudosSent} className="btn btn-outline-success">
            View Kudos Sent
          </button>
          <button onClick={kudosReceived} className="btn btn-outline-success">
            View Kudos Received
          </button>
          <button onClick={logout} className="btn btn-outline-danger">
            Log Out
          </button>
        </div>


        {kudosreceived.map(art => {
          return (
            <div className="list-group-item">
              <div>
                <span className="mr-3"><b>Sent by:</b></span>
                {art.sent_by.first_name} {art.sent_by.last_name}
              </div>   
              <div>
                <span className="mr-3"><b>Message:</b></span>
                {art.message}
              </div>
              <div>
                <span className="mr-3"><b>Date:</b></span>
                {art.created_at}
              </div>
            </div>
          );
        })}

        {kudossent.map(child => {
          return (
            <div className="list-group-item">
              <div>
                <span className="mr-3"><b>Sent to:</b></span>
                {child.sent_to.first_name} {child.sent_to.last_name}
              </div>              
              <div>
                <span className="mr-3"><b>Message:</b></span>
                {child.message}
              </div>
              <div>
                <span className="mr-3"><b>Date:</b></span>
                {child.created_at}
              </div>
            </div>
          );
        })}

      </div>
    </div>
  );
}

export default App;
