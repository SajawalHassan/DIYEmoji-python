import React from "react";
import "./Bottom.css";

import { CameraIcon, ClipboardIcon, UploadIcon } from "@heroicons/react/solid";

function Bottom() {
  return (
    <div className="bottom">
      <div className="bottom__center">
        <a href="#" title="Open webcam">
          <CameraIcon className="bottom__icon" />
        </a>
        <a href="#" title="Create filter">
          <ClipboardIcon className="bottom__icon" />
        </a>
        <a href="#" title="Upload photo">
          <UploadIcon className="bottom__icon" />
        </a>
      </div>
    </div>
  );
}

export default Bottom;
