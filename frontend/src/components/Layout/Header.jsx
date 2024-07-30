import React from "react";
import {
  SignedIn,
  SignedOut,
  SignInButton,
  UserButton,
} from "@clerk/clerk-react";

function Header() {
  return (
    <header className="w-full flex items-center justify-between">
      <div className="text-3xl">magical recipes</div>
      <div className="flex gap-5">
        {/* <SignedOut>
          <SignInButton />
        </SignedOut>
        <SignedIn>
          <UserButton />
        </SignedIn> */}
      </div>
    </header>
  );
}

export default Header;
