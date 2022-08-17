import React, {useState, useContext} from 'react'
import { Navbar } from './components/Navbar'
import Authcontext from "../context/Authcontext";

export const Registeruser = () => {
  const { error ,registerUser } = useContext(Authcontext);


  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(Userinfo);
    registerUser(Userinfo.username, Userinfo.fname, Userinfo.lname, Userinfo.email, Userinfo.password1, Userinfo.password2 )

  }

  const [Userinfo, setUserinfo] = useState({
    username: "",
    fname: "",
    lname: "",
    email: "",
    password1: "",
    password2: ""
  });

  const handleChange1 = (event) => {
    setUserinfo({ ...Userinfo, [event.target.name]: event.target.value });
  };

  return (
    <div>
      <Navbar />


      <div className='form-container'>

        <div className='container'>
          <h1 className='heading'> Register User </h1>

          <form>
            <fieldset>

              <div className="form-group">
                <label htmlFor="Name">Username:</label>
                <input type="text" className="form-control"  placeholder="Username" name='username' value={Userinfo.username} onChange={handleChange1} required={true} />
              </div>
              <small className='errormessage'>{error.errormessage.username}</small>

              <div className="form-group">
                <label htmlFor="Name">First Name:</label>
                <input type="text" className="form-control"  placeholder="First Name" name='fname' value={Userinfo.fname} onChange={handleChange1} required={true} />
              </div>

              <div className="form-group">
                <label htmlFor="Name">Last Name:</label>
                <input type="text" className="form-control"  placeholder="Last Naem" name='lname' value={Userinfo.lname} onChange={handleChange1} required={true} />
              </div>


              <div className="form-group">
                <label htmlFor="Name">Email:</label>
                <input type="email" className="form-control"  placeholder="email" name='email' value={Userinfo.email} onChange={handleChange1} required={true} />
              </div>
              <small className='errormessage'>{error.errormessage.email}</small>

              <div className="form-group">
                <label htmlFor="Name">Password:</label>
                <input type="password" className="form-control"  placeholder=" ******* " name='password1' value={Userinfo.password1} onChange={handleChange1} required={true} />
              </div>
              <small className='errormessage'>{error.errormessage.password}</small>

              <div className="form-group">
                <label htmlFor="Name">Conform Password:</label>
                <input type="password" className="form-control"  placeholder=" ******* " name='password2' value={Userinfo.password2} onChange={handleChange1} required={true} />
              </div>
              <div>
              <small className='errormessage'>{error.errormessage.password2}</small>
              </div>



              <button type="submit" className="btn btn-primary" onClick={handleSubmit}>Register</button>
            </fieldset>
          </form>

        </div>
      </div>
    </div>
  )
}
