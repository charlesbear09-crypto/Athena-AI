import * as THREE from "three";

import {OrbitControls}
from "three/addons/controls/OrbitControls.js";

import {GLTFLoader}
from "three/addons/loaders/GLTFLoader.js";


const scene = new THREE.Scene();

scene.background = new THREE.Color(0x111111);



const camera =
new THREE.PerspectiveCamera(
45,
window.innerWidth/window.innerHeight,
0.1,
1000
);


camera.position.set(5,3,8);



const renderer =
new THREE.WebGLRenderer({

canvas:document.getElementById("bg"),

antialias:true

});


renderer.setSize(
window.innerWidth,
window.innerHeight
);



const controls =
new OrbitControls(
camera,
renderer.domElement
);

controls.enableDamping=true;



const light =
new THREE.HemisphereLight(
0xffffff,
0x444444,
2
);

scene.add(light);



const dir =
new THREE.DirectionalLight(
0xffffff,
3
);

dir.position.set(5,10,5);

scene.add(dir);



const loader =
new GLTFLoader();



loader.load(

"../models/silverado.glb",

function(gltf){

const truck = gltf.scene;

scene.add(truck);

truck.position.set(0,0,0);

truck.scale.set(1,1,1);

},

undefined,

function(error){

console.log(error);

alert("Couldn't load Silverado model.");

}

);



function animate(){

requestAnimationFrame(animate);

controls.update();

renderer.render(scene,camera);

}

animate();



window.addEventListener(

"resize",

()=>{

camera.aspect=
window.innerWidth/window.innerHeight;

camera.updateProjectionMatrix();

renderer.setSize(

window.innerWidth,

window.innerHeight

);

}

);
