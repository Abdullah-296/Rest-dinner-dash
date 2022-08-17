import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import {useNavigate} from 'react-router-dom';

const Authcontext = createContext();

export default Authcontext;


export const AuthProvider = ({ children }) => {

  const navigate = useNavigate();

  const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  const [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwt_decode(localStorage.getItem("authTokens"))
      : null
  );

  const [error, setError] = useState(
    {
      'errors': false,
      'errormessage': []
    }
  )


  const logout = () => {
    console.log(authTokens);
    console.log(user);
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    console.log(authTokens);
    console.log(user);
    navigate('/');
  }


  const registerUser = async (username, first_name, last_name, email, password, password2) => {
    const response = await fetch("http://localhost:8000/api/registeruser/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify({
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "password2": password2
      })
    });
    const data = await response.json();

    if (response.status === 201) {
      console.log('User registered');
      navigate('/');
    } else {
      console.log(data);
      setError(
        {
          'errors': true,
          'errormessage': data,
          }
      )

    }
  };

  const loginUser = async (username, password) => {
    const response = await fetch("http://localhost:8000/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "username": username,
        "password": password
      })
    });

    const data = await response.json();

    if (response.status === 200) {

      setAuthTokens(data);
      setUser(jwt_decode(data.access));

      console.log(data);
      console.log(jwt_decode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));

      navigate('/admin');

    } else {
      alert("Something went wrong!");
    }
  };

  const [loading, setLoading] = useState(true);


  useEffect(() => {
    if (authTokens) {
      setUser(jwt_decode(authTokens.access));
    }
    setLoading(false);
  }, [authTokens, loading]);

  const contextData = {
    user,
    setUser,
    authTokens,
    setAuthTokens,
    loginUser,
    logout,
    registerUser,
    error
  };

  return (
    <Authcontext.Provider value={contextData}>
      {loading ? null : children}
    </Authcontext.Provider>
  );


}
