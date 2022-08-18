import { useContext } from "react";
import Authcontext from "../context/Authcontext";
import { Navigate, Outlet } from 'react-router-dom';

export const Protectedroute = () => {
  let { user } = useContext(Authcontext);
  return user ? <Outlet /> : <Navigate to="/Login" />;
}

