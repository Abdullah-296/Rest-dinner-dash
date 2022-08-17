import React from 'react'

export const Orderlist = (props) => {
  const length = props.order.items.length;
  return (
    <div className='container'>



        <table className="table table-striped">
          <thead>
            <tr>
              <th scope="col">Order ID: {props.order.id} </th>
              <th scope="col">Status: {props.order.status}</th>
            </tr>
          </thead>
          </table>

          { length !== 0 &&

            <table className="table table-striped">
              <thead>
                <tr>
                  <th scope="col">orderitem Id </th>
                  <th scope="col">item id</th>
                  <th scope="col">item order</th>
                  <th scope="col">item quantity</th>
                </tr>
              </thead>
              <tbody>



            { length !== 0 &&
              props.order.items.map((item) =>
              <tr key={item.id}>

                <td>{item.id}</td>
                <td>{item.item}</td>
                <td>{item.order}</td>
                <td>{item.quantity}</td>

              </tr>
              )
            }
        </tbody>
      </table>
      }

    </div>
  )
}
