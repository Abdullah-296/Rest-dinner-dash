import React, {useState, useContext} from 'react'
import { Navbar } from './components/Navbar'
import Authcontext from "../context/Authcontext";

export const Registeruser = () => {
  const { error ,registerUser } = useContext(Authcontext);


  const handleSubmit = (e) => {
    e.preventDefault()
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


  const [fielderror, setfielderror] = useState({
    username: false,
    fname: false,
    lname: false,
    email: false,
    password1: false,
    password2: false,
  });

  const handleChange1 = (event) => {
    setUserinfo({ ...Userinfo, [event.target.name]: event.target.value });
    checkvalidation(event)
  };

  const checkvalidation = (event) => {
      if ((event.target.name === 'password1' || event.target.name === 'password2')  && (event.target.value.length < 8 || event.target.value.length > 32)){
        setfielderror({ ...fielderror, [event.target.name]: true})
      }
      else if(event.target.value.length < 2 || event.target.value.length > 32)
      {
        setfielderror({ ...fielderror, [event.target.name]: true})
      }
      else {
        setfielderror({ ...fielderror, [event.target.name]: false})
      }
  }

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
              {fielderror.username && <small className='errormessage'> Make sure length is between 2 and 32.</small>}

              <div className="form-group">
                <label htmlFor="Name">First Name:</label>
                <input type="text" className="form-control"  placeholder="First Name" name='fname' value={Userinfo.fname} onChange={handleChange1} required={true} />
              </div>
              {fielderror.fname && <small className='errormessage'> Make sure length is between 2 and 32.</small>}


              <div className="form-group">
                <label htmlFor="Name">Last Name:</label>
                <input type="text" className="form-control"  placeholder="Last Naem" name='lname' value={Userinfo.lname} onChange={handleChange1} required={true} />
              </div>
              {fielderror.lname && <small className='errormessage'> Make sure length is between 2 and 32.</small>}


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
              {fielderror.password1 && <small className='errormessage'> Make sure length is between 8 and 32.</small>}


              <div className="form-group">
                <label htmlFor="Name">Conform Password:</label>
                <input type="password" className="form-control"  placeholder=" ******* " name='password2' value={Userinfo.password2} onChange={handleChange1} required={true} />
              </div>
              {fielderror.password2 && <small className='errormessage'> Make sure length is between 8 and 32.</small>}

              <div>
              <small className='errormessage'>{error.errormessage.password2}</small>
              </div>

              <button type="submit"
              className="btn btn-primary"
              onClick={handleSubmit}
              disabled={(fielderror.username || fielderror.fname || fielderror.lname || fielderror.password1 || fielderror.password2
                      || Userinfo.username.length === 0 || Userinfo.fname.length === 0 || Userinfo.lname.length === 0 || Userinfo.password1.length === 0 || Userinfo.password2.length === 0 || Userinfo.email.length === 0) }
              >Register</button>

            </fieldset>
          </form>

        </div>
      </div>
    </div>
  )
}
