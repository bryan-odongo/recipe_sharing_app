import React, { useRef, useState } from "react";
import Layout from "../../components/Layout/Layout";
import { BsArrowDownRight } from "react-icons/bs";
import clsx from "clsx";

import advideo from "../../assets/video/digital.mp4";

function Register() {
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password !== repeatPassword) {
      setError("Passwords do not match");
      return;
    }

    // Perform registration logic here
    console.log("Registration submitted:", {
      firstname,
      lastname,
      email,
      password,
    });

    // Reset form fields
    setFirstname("");
    setLastname("");
    setEmail("");
    setPassword("");
    setRepeatPassword("");
  };

  return (
    <Layout>
      <div className="relative w-screen h-screen  flex justify-start items-center">
        <div className={clsx("relative z-20 w-1/3 h-full bg-black")}></div>
        <div
          className={clsx(
            "relative z-20 w-2/3 h-[calc(100vh)] grid grid-cols-6 grid-rows-6 gap-3 p-5 bg-transparent"
          )}
        >
          <span className="col-start-1 col-span-1 row-start-1 row-span-1 bg-transparent border-4 border-lime-600 rounded-b-xl rounded-tl-3xl"></span>
          <span className="col-start-2 col-span-2 row-start-1 row-span-1 bg-black rounded-b-xl"></span>
          <span className="col-start-4 col-span-2 row-start-1 row-span-1 bg-black rounded-b-xl"></span>
          <span className="col-start-6 col-span-1 row-start-1 row-span-1 bg-transparent border-4 border-yellow-600 rounded-b-xl rounded-tr-3xl"></span>
          <span className="col-start-1 col-span-1 row-start-2 row-span-2 bg-black rounded-r-xl"></span>
          <span className="col-start-2 col-span-2 row-start-2 row-span-2 bg-transparent border-4 border-white rounded-xl"></span>
          <span className="col-start-4 col-span-2 row-start-2 row-span-2 bg-yellow-300 rounded-xl"></span>
          <span className="col-start-6 col-span-1 row-start-2 row-span-2 bg-black rounded-xl"></span>
          <span className="col-start-1 col-span-1 row-start-4 row-span-2 bg-black rounded-r-xl"></span>
          <span className="col-start-2 col-span-2 row-start-4 row-span-2 bg-yellow-300 rounded-xl"></span>
          <span className="col-start-4 col-span-2 row-start-4 row-span-2 bg-transparent border-4 border-blue-600 rounded-xl"></span>
          <span className="col-start-6 col-span-1 row-start-4 row-span-2 bg-black rounded-xl"></span>{" "}
          <span className="col-start-1 col-span-1 row-start-6 row-span-1 bg-transparent border-4 border-cyan-600 rounded-t-xl rounded-bl-3xl"></span>
          <span className="col-start-2 col-span-2 row-start-6 row-span-1 bg-black rounded-t-xl"></span>
          <span className="col-start-4 col-span-2 row-start-6 row-span-1 bg-black rounded-t-xl"></span>
          <span className="col-start-6 col-span-1 row-start-6 row-span-1 bg-transparent border-4 border-red-600 rounded-t-xl rounded-br-3xl"></span>
        </div>
      </div>
      <Video />
    </Layout>
  );
}

const Video = () => {
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);

  return (
    <div className="absolute inset-0 h-[100%] flex items-center justify-center w-full bg-black">
      <video
        ref={videoRef}
        onPlay={() => setIsPlaying(true)}
        onPause={() => setIsPlaying(false)}
        className="object-cover w-full h-[100%] rounded-r-[4rem] border-t-[32px] border-b-[32px] border-r-[32px] border-black"
        src={advideo}
        muted
        autoPlay
        loop
      />
      {!isPlaying && (
        <button
          onClick={() => videoRef.current.play()}
          className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-black bg-opacity-50 rounded-full p-4"
        >
          <BsArrowDownRight className="text-white text-4xl" />
        </button>
      )}
    </div>
  );
};

export default Register;
