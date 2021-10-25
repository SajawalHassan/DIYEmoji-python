import React from "react";
import "./Main.css";

import profile_pic from "./images/profilepic.jpg";

function main() {
  return (
    <div className="main">
      {/* ADD WHEN HAVE ACTUAL AUTH */}
      {/* <div className="main__header">
        <div className="main__headerLeft">
          <h1>DIY Filters</h1>
        </div>
        <div className="main__headerRight">
          <button>Login</button>
        </div>
      </div> */}

      <div className="main__body">
        {/* WILL CHANGE TO AUTHENTICATOR IMG */}
        <img src={profile_pic} alt="" />
      </div>
    </div>
  );
}

export default main;
