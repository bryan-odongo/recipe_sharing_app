import React from "react";
import bg from "../../assets/imgs/shape3-min.png";

function Banner() {
  return (
    <section className="relative h-[75vh] w-full bg-pink-200 bg-[]">
      <img
        src={bg}
        alt="banner_bg"
        className="absolute top-0 left-0 w-full h-full object-cover"
      />
      <div className="w-full h-full lg:px-12 xl:container mx-auto absolute top-[2rem] left-0 space-y-7 flex flex-col justify-center items-end bg-transparent">
        <div className="banner_text w-full h-fit flex justify-end items-center">
          <h1 className="w-full flex flex-col justify-items-center leading-[4rem] trac [&_span]:font-bold [&_span]:text-right [&_span]:text-[3.8rem]">
            <span className="">Fresh Flavors, Nutritional</span>
            <span>values, ready for all your</span>
            <span>health needs</span>
          </h1>
        </div>

        <div className="small_text pt-5 max-w-[356px] border-t-2 border-black">
          <p className="font-semibold  ">
            Neque porro quisquam est qui dolorem ipsum quia dolor sit amet,
            consectetur, adipisci velit. Mauris metus dui, molestie iaculis
            dolor et, malesuada fermentum diam.
          </p>
        </div>
      </div>
    </section>
  );
}

export default Banner;
