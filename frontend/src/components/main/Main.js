import React from "react";
import "./Main.css";

import profile_pic from "./images/profilepic.jpg";

function main() {
  return (
    <div className="main">
      <div className="main_body">
        {/* WILL CHANGE TO AUTHENTICATOR IMG */}
        <img src={profile_pic} alt="" />
      </div>
    </div>
  );
}

export default main;
