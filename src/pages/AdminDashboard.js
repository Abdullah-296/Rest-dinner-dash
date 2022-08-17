import React, { useEffect, useState } from 'react'
import {Navbar} from './components/Navbar';
import {Hero} from './components/Hero';
import { Orderlist } from './components/OrderComponents/Orderlist';
import { useContext } from "react";

import useAxios from "../context/useAxios";


export const AdminDashboard = () => {
  const [res, setRes] = useState("");
  const [orders, setOrder] = useState([])
  const api = useAxios();



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/orders/");
        setRes(response.data.message);
        setOrder(response.data)
      } catch {
        setRes("Something went wrong");
      }
    };

    fetchData();
  }, []);


  return (
    <div>
      <Navbar />
      <Hero />
      <div className='container'>
        <table className="table">
          <thead className="thead-dark">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Orders List</th>
            </tr>
          </thead>
        </table>
      </div>


      {orders && orders.map((order) =>
      <Orderlist key={order.id} order={order} />
      )}

    </div>
  )
}
