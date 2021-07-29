# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file automatically generates and saves a series of example pictures for the 
circuit drawer.  This will be useful during early stages when the project is still
undergoing cosmetic changes.
"""

import matplotlib.pyplot as plt

from pennylane.beta.circuit_drawer import MPLDrawer


def just_wires(savefile="example_pics/just_wires.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=1)
    drawer.wires()
    plt.savefig(savefile)


def labels(savefile="example_pics/labels.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=1)
    drawer.wires()
    drawer.label(["a", "b"])
    plt.savefig(savefile)


def box_gates(savefile="example_pics/box_gates.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=2)
    drawer.wires()

    drawer.box_gate(layer=0, wires=0, text="Y")
    drawer.box_gate(layer=1, wires=(0, 1), text="CRy(0.1)", rotate_text=True)
    plt.savefig(savefile)


def ctrl(savefile="example_pics/ctrl.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=2)
    drawer.wires()

    drawer.ctrl(layer=0, wire_ctrl=0, wire_target=1)
    drawer.ctrl(layer=1, wire_ctrl=(0, 1))
    plt.savefig(savefile)


def CNOT(savefile="example_pics/cnot.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=2)
    drawer.wires()

    drawer.CNOT(0, (0, 1))
    drawer.CNOT(1, (1, 0))
    plt.savefig(savefile)


def target_x(savefile="example_pics/target_x.png"):
    drawer = MPLDrawer(n_wires=1, n_layers=1)
    drawer.wires()
    drawer._target_x(0, 0)
    plt.savefig(savefile)


def SWAP(savefile="example_pics/SWAP.png"):
    drawer = MPLDrawer(n_wires=2, n_layers=1)
    drawer.wires()

    drawer.SWAP(0, (0, 1))
    plt.savefig(savefile)


def swap_x(savefile="example_pics/swap_x.png"):
    drawer = MPLDrawer(n_wires=1, n_layers=1)
    drawer.wires()

    drawer._swap_x(0, 0)
    plt.savefig(savefile)


def measure(savefile="example_pics/measure.png"):
    drawer = MPLDrawer(n_wires=1, n_layers=1)
    drawer.wires()

    drawer.measure(0, 0)
    plt.savefig(savefile)


just_wires()
labels()
box_gates()
ctrl()
CNOT()
target_x()
SWAP()
swap_x()
measure()
