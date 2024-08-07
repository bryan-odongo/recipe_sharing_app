import React, { useState } from "react";
import Layout from "../../components/Layout/Layout";
import { SignIn } from "@clerk/clerk-react";

function Login() {
  const [isSingIn, setIsSignIn] = useState(true);
  return (
    <Layout>
      <section className="w-full min-h-[calc(100vh-156px)]">
        <div className="bg-red-800 h-full  max-w-4xl xl:max-w-[73rem] w-full mx-auto py-3 flex justify-between items-center">
          <SignIn signInFallbackRedirectUrl={"/recipes"} />
        </div>
      </section>
    </Layout>
  );
}

export default Login;
