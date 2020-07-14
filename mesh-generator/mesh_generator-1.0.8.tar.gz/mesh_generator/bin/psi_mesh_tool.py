"""This is a translation of the FORTRAN mesh psi_tool.
Generate a one-dimensional mesh.
Input: tmp_mesh_[t/p/r].dat (legacy mesh results)
Output: mesh_res_[t/p/r].txt (a file with mesh points).
"""
import numpy as np


def write_mesh_res_file(dir_name, output_file_name, input_file_path):
    """Writes a file with mesh points, respective resolution, and cell-to-cell ratio.
    :param input_file_path: input file path.
    :param output_file_name: output filename.
    :param dir_name: directory to write the output file.
    :return: mesh_res_[t/p/r].txt (a file with mesh points).
    """
    # Open the input file.
    with open(input_file_path, 'r') as f:
        input_data = f.readlines()

    # *** GET PARAMS ***
    # Get the coordinate label
    label = input_data[1].rstrip('\n')[0]
    # Get the flag to indicate a periodic mesh.
    periodic = input_data[3].rstrip(' \n')
    # Get the number of mesh points.
    nx = int(input_data[5].rstrip('\n'))
    x = [None] * nx
    # Get the domain limits.
    x0 = float(input_data[7].rstrip('\n').split(",")[0])
    x1 = float(input_data[7].rstrip('\n').split(",")[1])
    # Get the node positions.
    xfrac = input_data[9].rstrip('\n')
    xfrac = xfrac[:len(xfrac) - 2]
    xfrac = xfrac.split(",")
    xfrac = [float(item) for item in xfrac]
    #  Calculate the number of nodes set.
    n_seg = len(xfrac)
    # Get the magnification factors.
    dxratio = input_data[11].rstrip('\n')
    dxratio = dxratio[:len(dxratio) - 2]
    dxratio = dxratio.split(",")
    dxratio = [float(item) for item in dxratio]
    # Get the shift amount.
    xshift = float(input_data[13].rstrip('\n'))
    # Get the number of times to filter the mesh.
    nfilt = int(input_data[-1])

    io = 0
    nmseg = 100

    # Generate the mesh.
    c = genmesh(io, label, nx, x0, x1, n_seg, xfrac, dxratio, nfilt, periodic, xshift, x)


def genmesh(io, label, nc, c0, c1, nseg, frac, dratio, nfilt, periodic, c_shift, c):
    """Generate a 1D Mesh.
    Input arguments:
            IO      : [integer]
                       Fortran file unit number to which to write
                       mesh diagnostics.  Set IO=0 if diagnostics
                       are not of interest.  It is assumed that
                       unit IO has been connected to a file prior
                       to calling this routine.

            LABEL   : [character(*)]
                      Name for the mesh coordinate (example: 'x').

            NC      : [integer]
                      Number of mesh points to load.

            C0      : [real]
                      The starting location for the coordinate.

            C1      : [real]
                      The ending location for the coordinate.
                      It is required that C1.gt.C0.

            NSEG    : [integer]
                       Maximum number of mesh segments.
                       The mesh spacing in each segment varies
                       exponentially with a uniform amplification
                       factor.  The actual number of mesh segments
                       used is NSEG or less.  It is obtained from the
                       information in array FRAC.

            FRAC    : [real array, dimension NSEG]
                       The normalized positions of the mesh segment
                       boundaries (as a fraction of the size of the
                       domain).  For a non-periodic mesh, the first
                       value of FRAC specified must equal 0. and the
                       last value must equal 1.  For a periodic mesh,
                       FRAC must not contain both 0. and 1., since
                       these represent the same point.

            DRATIO  : [real array, dimension NSEG]
                       The ratio of the mesh spacing at the end of a
                       segment to that at the beginning.

            NFILT   : [integer]
                      The number of times to filter the mesh-point
                      distribution array.  Set NFILT=0 if filtering
                      is not desired.  Filtering can reduce
                      discontinuities in the derivative of the mesh
                      spacing.

            PERIODIC: [logical]
                       A flag to indicate whether the mesh to be
                       generated represents a periodic coordinate.
                       If the coordinate is specified as periodic,
                       the range [C0,C1] should be the whole periodic
                       interval; the first mesh point is set at C0
                       and the last mesh point, C(NC), is set at C1.

            C_SHIFT : [real]
                       Amount by which to shift the periodic coordinate.
                       C_SHIFT is only used when PERIODIC=.true.,
                       and is ignored otherwise.  A positive C_SHIFT
                       moves the mesh points to the right.

    Output arguments:

             C       : [real array, dimension NC]
                       The locations of the mesh points.
    """

    eps = 10 ** -5
    # Check that the number of mesh points is valid.
    if nc < 2:
        print('### ERROR in GENMESH:\n### Invalid number of mesh points specified.\n' +
              '### There must be at least two mesh points.\nMesh coordinate: ' + str(label) +
              '. Number of mesh points specified = ' + str(nc))
        return

    # Check that a positive mesh interval has been specified.
    if c0 >= c1:
        print('### ERROR in GENMESH:\n' + '### Invalid mesh interval specified.\n' + '### C1 must be greater than C0.' +
              ' Mesh coordinate: ' + str(label) + ', C0 = ' + str(c0) + ', C1 = ' + str(c1))
        return

    # Find the number of values of FRAC specified.
    # TODO: Make sure this is right.
    for nf in range(1, nseg):
        if frac[nf] == 0.:
            break

    # When no values have been specified (NF=1, the default), a uniform mesh is produced.
    if nf == 1. and frac[0] == 0.:
        cs = [c0, c1]
        r = [1]

    # Check that the specified values of FRAC are monotonically increasing.
    for i in range(1, nseg):
        if frac[i] < frac[i - 1]:
            print('### ERROR in GENMESH:')
            print('### Invalid mesh specification.')
            print('Mesh coordinate: ', label)
            print('The values in FRAC must increase monotonically.')
            print('FRAC = ', frac)
            return

    # Check the specified values of FRAC.
    if periodic == ".true.":
        if frac[0] < 0. or frac[-1] > 1.:
            # A periodic mesh requires the specified values of FRAC to be in the range 0. to 1.
            print('### ERROR in GENMESH:')
            print('### Invalid mesh specification.')
            print('Mesh coordinate: ', label)
            print('For a periodic coordinate, the values in FRAC must be between 0. and 1.')
            print('FRAC = ', frac)
            return

        if frac[0] == 0. and frac[-1] == 1.:
            # A periodic mesh cannot contain both 0. and 1. in FRAC, since these represent the same point.
            print('### ERROR in GENMESH:')
            print('### Invalid mesh specification.')
            print('Mesh coordinate: ', label)
            print('For a periodic coordinate, the values in FRAC must not contain both 0. and 1.')
            print('FRAC = ', frac)
            return

    if periodic == ".false.":
        # A non-periodic mesh requires the first specified value of FRAC to be 0., and the last value to equal 1.
        if frac[0] != 0.:
            print('### ERROR in GENMESH:')
            print('### Invalid mesh specification.')
            print('Mesh coordinate: ', label)
            print('For a non-periodic coordinate, the first value of FRAC must equal 0. ')
            print('FRAC = ', frac)
            return

        if frac[-1] != 1.:
            print('### ERROR in GENMESH:')
            print('### Invalid mesh specification.')
            print('Mesh coordinate: ', label)
            print('For a non-periodic coordinate, the last value of FRAC must equal 1. ')
            print('FRAC = ', frac)
            return

    # Check that the required values of DRATIO have been set, and are positive.
    if periodic == ".true.":
        nr = nf
    else:
        nr = nf - 1
#
#     i = 0
#     for i in range(0, nr):
#         if dratio[i] < zero:
#             print('### ERROR in GENMESH:')
#             print('### Invalid mesh specification.')
#             print('Mesh coordinate: ', label)
#             print('A required value in DRATIO has not been set or is not positive.')
#             print('DRATIO = ', dratio)
#             return
#
#     # Check that an inherently discontinuous mesh has not been
#     if periodic == ".true." and nr == 1 and dratio[0] != zero:
#         print('### WARNING from GENMESH:')
#         print('### Discontinuous mesh specification.')
#         print('Mesh coordinate: ', label)
#         print('An inherently discontinuous mesh has been specified.')
#         print('FRAC = ', frac)
#         print('DRATIO = ', dratio)
#
#     # Set the number of segments
#     ns = nf - 1
#
#     # For a periodic coordinate, add points at XI=0. and XI=1. If they are not already present.
#     if periodic == ".true.":
#         if frac[0] != zero:
#             ns = ns + 1
#         if frac[-1] != one:
#             ns = ns + 1
#
#     cs = [None] * (ns + 1)
#     r = [None] * ns
#
#     # Set up the coordinate limits of the segments.
#     if periodic == ".true.":
#         if frac[0] != 0.:
#             cs[0] = c0
#             cs[1:] = [c0 + (c1 - c0) * x for x in frac]
#             if frac[-1] != 1.:
#                 alpha = (one - frac[-1]) / (frac[0] + one - frac[-1])
#                 r[0] = dratio[nr - 1] / (one + alpha * (dratio[nr - 1] - one))
#                 r[1:nr] = dratio[0:nr]
#                 cs[-1] = c1
#                 r[-1] = 1. + alpha * (dratio[-1] - 1)
#             else:
#                 r[0] = dratio[nr - 1]
#                 r[1:] = dratio[:nr - 2]
#         else:
#             cs[:nf] = [c0 + (c1 - c0) * x for x in frac]
#             r[:nr] = dratio[:nr]
#             cs[-1] = c1
#     else:
#         cs = [c0 + (c1 - c0) * x for x in frac]
#         r[:nr] = dratio[:nr]
#
#     # allocate xi, a, f
#     xi = [None] * (ns + 1)
#     a = [None] * ns
#     f = [None] * ns
#
#     # Compute the XI values at the segment limits.
#     for i in range(0, ns):
#         dr = r[i] - one
#         if abs(dr) < eps:
#             f[i] = (cs[i + 1] - cs[i]) * (1. + 0.5 * dr)
#         else:
#             f[i] = (cs[i + 1] - cs[i]) * np.log10(r[i]) / dr
#
#     fac = zero
#     for i in range(ns - 1, 0, -1):
#         fac = fac / r[i] + f[i]
#
#     d = f[0] / fac
#     xi[0] = zero
#     for i in range(1, ns):
#         xi[i] = xi[i - 1] + d
#         if i < ns:
#             d = d * f[i] / (f[i - 1] * r[i - 1])
#     xi[-1] = one
#
#     # Set the amplification factor for each segment.
#     for i in range(0, ns):
#         a[i] = np.log10(r[i] / (xi[i + 1] - xi[i]))
#
#     # For a periodic coordinate, find the XI shift corresponding to a shift of C_SHIFT in the coordinate.
#     # Note that a positive value of C_SHIFT moves the mesh points to the right.
#     if periodic == ".true.":
#         cshft = -c_shift
#         xi_shift = map_c_to_xi(periodic, ns, xi, cs, a, r, cshft, eps)
#     else:
#         xi_shift = 0.
#
#     # Compute the location of the mesh points in array C by mapping from the XI values.
#     dxi = one / (nc - one)
#
#     c = [None] * nc
#     c[0] = c0
#     for j in range(1, nc - 2):
#         xiv = (j - 1) * dxi
#         print(j)
#         c[j] = map_xi_to_c(periodic, ns, xi, cs, a, r, cshft, xi_shift, xiv, c[j], eps)
#     c[nc - 1] = c1
#
#     # Filter the mesh if requested
#     if nfilt > 0:
#         for i in range(0, nfilt):
#             if periodic == ".true.":
#                 f = filter_coord_periodic(c1 - c0, nc, c)
#             else:
#                 f = filter_coord(nc, c)
#
#
# def filter_coord(n, f):
#     """
#     Apply a "(1,2,1)/4" low-pass digital filter to a 1D coordinate.
#     The end-points F(1) and F(N) are not changed.
#     """
#     # Make a copy of the function.
#     ff = f
#
#     # Apply the filter.
#     for i in range(1, n - 1):
#         f[i] = 0.25 * (ff[i - 1] + 2. * ff[i] + ff[i + 1])
#
#     return f
#
#
# def filter_coord_periodic(xl, n, f):
#     """
#     Apply a "(1,2,1)/4" low-pass digital filter to a periodic 1D coordinate.
#     XL is the periodic interval for the coordinate.
#     The filtered coordinate is translated so that F(1) is preserved.
#     """
#     ff = [None] * (n + 1)
#     # Save the value of F(1).
#     f1old = f[0]
#     # Make a periodic copy of the function.
#     ff[1: n] = f
#     ff[0] = f[int(n - 2)] - xl
#     ff[n] = f[1] + xl
#     # Apply the filter:
#     for i in range(1, n):
#         f[i] = 0.25 * (ff[i - 1] + 2. * ff[i] + ff[i + 1])
#     # Translate F so that F(1) is preserved.
#     f1new = f[0]
#     for i in range(1, n):
#         f[i] = f[i] - f1new + f1old
#     return f
#
#
# def map_xi_to_c(periodic, ns, xi, cs, a, r, cshft, xi_shift, xiv, cv, eps):
#     """
#     Get the mesh coordinate value CV for the specified xi value XIV.
#     Set PERIODIC=.true. for a periodic coordinate. NS is the number of segments in the mesh definition.
#     The arrays XI, CS, A, and R define the mesh mapping.
#     CSHFT represents the amount to shift a periodic coordinate.
#     XI_SHIFT represents the corresponding amount to shift xi.
#     This is a utility routine for GENMESH.
#     """
#     # Find the index of the segment to which XIV belongs.
#     if periodic == ".true.":
#         # Shift XIV by XI_SHIFT.
#         xiv_p = xiv + xi_shift
#         # Fold XIV_P into the main interval.
#         xiv_p = fold(0., 1., xiv_p)
#     else:
#         xiv_p = xiv
#
#     for i in range(0, ns):
#         if xi[i] <= xiv_p <= xi[i + 1]:
#             break
#
#     if i > ns:
#         print('### ERROR in MAP_XI_TO_C:')
#         print('### Error in finding the XI segment.')
#         print('### Could not find XIV in the XI table.')
#         print('[Utility routine for GENMESH.]')
#         print('[This is an internal error.]')
#         print('XI = ', xi)
#         print('XIV = ', xiv)
#         print('XIV_P = ', xiv_p)
#
#     d = xiv_p - xi[i]
#     d1 = xi[i + 1] - xi[i]
#     da = a[i] * d
#     da1 = a[i] * d1
#
#     # Interpolate the mapping function at XIV_P.
#     if abs(da1) < eps:
#         fac = (d * (1. + 0.5 * da)) / (d1 * (1 + 0.5 * da1))
#     else:
#         print(r[i])
#         print(da)
#         fac = (np.exp(da) - 1.) / (r[i] - 1.)
#     cv = cs[i] + (cs[i + 1] - cs[i]) * fac
#
#     if periodic == ".true.":
#         # Shift CV by the amount CSHFT.
#         cv = cv - cshft
#         # Fold CV into the main interval.
#         cv = fold(cs[0], cs[ns], cv)
#     return cv
#
#
# def map_c_to_xi(periodic, ns, xi, cs, a, r, cv, eps):
#     """
#     Get the xi value XIV for the specified coordinate value CV.
#     Set PERIODIC=.true. for a periodic coordinate.
#     NS is the number of segments in the mesh definition.
#     The arrays XI, CS, A, and R define the mesh mapping.
#     This is a utility routine for GENMESH.
#     """
#     # Find the index of the segment to which CV belongs.
#     if periodic == ".true.":
#         # Fold CV_P into the main interval.
#         cv_p = fold(cs[0], cs[-1], cv)
#     else:
#         cv_p = cv
#
#     for i in range(0, ns):
#         if cs[i] <= cv_p <= cs[i + 1]:
#             break
#
#     if i > ns:
#         print('### ERROR in MAP_C_TO_XI:')
#         print('### Error in finding the CS segment.')
#         print('### Could not find CV in the CS table.')
#         print('[Utility routine for GENMESH.]')
#         print('[This is an internal error.]')
#         print('CS = ', cs)
#         print('CV = ', cv)
#         print('CV_P = ', cv_p)
#         return
#
#     d = (cv_p - cs[i]) / cs[i + 1] - cs[i]
#     da = (r[i] - 1.) * d
#
#     # Interpolate the mapping function at XIV_P.
#     if abs(da) < eps:
#         fac = d * (xi[i + 1] - xi[i])
#     else:
#         fac = np.log10(da + 1.) / a[i]
#
#     xiv = xi[i] + fac
#     return xiv
#
#
# def fold(x0, x1, x):
#     """
#     "Fold" X into the periodic interval [X0,X1].
#     On return, X is such that X0.le.X.lt.X1.
#     It is assumed that X0 does not equal X1, as is physically necessary.
#     If X0 and X1 are equal, the routine just returns with FOLD=X.
#     :param x0: begin mesh coordinate
#     :param x1: end mesh coordinate
#     :param x: shift
#     :return:
#     """
#     fold = x
#     if x0 == x1:
#         return fold
#     xl = x1 - x0
#     fold = ((x - x0) % xl) + x0
#     if fold < x0:
#         fold = fold + xl
#     if fold > x1:
#         fold = fold - xl
#     return fold
#

if __name__ == "__main__":
    import os

    write_mesh_res_file(os.getcwd(), os.path.join(os.getcwd(), "mesh_res_t.dat"),
                        os.path.join(os.getcwd(), "tmp_mesh_t.dat"))
