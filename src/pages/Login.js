import React, { useContext } from 'react'
import { Navbar } from './components/Navbar'
import Authcontext from "../context/Authcontext";

export const Login = () => {
  const { loginUser, logout } = useContext(Authcontext);

  const handleSubmit = (e) => {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
    loginUser(username, password);
  }



  return (
    <div>
      <Navbar />


      <div className='form-container'>

        <div className='container'>
          <h1 className='heading'> Login User </h1>


          <form onSubmit={handleSubmit}>

            <hr />
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input className="form-control" type="text" id="username" placeholder="Enter Username" />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input className="form-control" type="password" id="password" placeholder="Enter Password" />
            </div>

            <button className="btn btn-primary" type="submit">Login</button>
          </form>


        </div>
      </div>
    </div>
  )
}
