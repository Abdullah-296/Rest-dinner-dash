import React from 'react'
import { Outlet, Link } from "react-router-dom";


export const PageNotFound = () => {
  return (
    <div>
      <h2> 404 error</h2>
      <h6> Page not found, kindly add valid url.</h6>
      <Outlet />
    </div>
  )
}
