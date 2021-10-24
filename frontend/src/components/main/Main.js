import React from "react";
import "./Main.css";

import { MicrophoneIcon } from "@heroicons/react/solid";
import profile_pic from "./images/profilepic.jpg";

function main() {
  return (
    <div className="main">
      <div className="main_header">
        <MicrophoneIcon className="icon" />
      </div>

      <div className="main_body">
        {/* WILL CHANGE TO AUTHENTICATOR IMG */}
        <img src={profile_pic} alt="" />
      </div>
    </div>
  );
}

export default main;
