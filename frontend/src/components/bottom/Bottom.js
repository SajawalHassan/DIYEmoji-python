import React from "react";
import "./Bottom.css";

import { CameraIcon, ClipboardIcon, UploadIcon } from "@heroicons/react/solid";

function Bottom() {
  let day = new Date().getDate();
  let month = new Date().getMonth();

  return (
    <div className="bottom">
      <div className="bottom__date">
        <p>
          Date: 21-{month}-{day}
        </p>
      </div>
      <div className="bottom__center">
        <a href="#" title="Open webcam">
          <CameraIcon className="bottom__centerIcon" />
        </a>
        <a href="#" title="Create filter">
          <ClipboardIcon className="bottom__centerIcon" />
        </a>
        <a href="#" title="Upload photo">
          <UploadIcon className="bottom__centerIcon" />
        </a>
      </div>
    </div>
  );
}

export default Bottom;
